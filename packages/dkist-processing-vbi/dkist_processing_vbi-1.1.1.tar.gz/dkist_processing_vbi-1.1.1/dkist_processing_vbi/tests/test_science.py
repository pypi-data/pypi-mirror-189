import json

import numpy as np
import pytest
from astropy.io import fits
from dkist_processing_common._util.scratch import WorkflowFileSystem
from dkist_processing_common.models.tags import Tag
from dkist_processing_common.tests.conftest import FakeGQLClient

from dkist_processing_vbi.models.tags import VbiTag
from dkist_processing_vbi.parsers.vbi_l0_fits_access import VbiL0FitsAccess
from dkist_processing_vbi.tasks.science import ScienceCalibration
from dkist_processing_vbi.tests.conftest import ensure_all_inputs_used
from dkist_processing_vbi.tests.conftest import generate_214_l0_fits_frame
from dkist_processing_vbi.tests.conftest import Vbi122ObserveFrames
from dkist_processing_vbi.tests.conftest import VbiConstantsDb


@pytest.fixture(scope="function")
def science_calibration_task(tmp_path, recipe_run_id, init_vbi_constants_db, abort_mosaic):
    num_steps = 4
    num_dsps_repeats = 3
    num_exp_per_step = 2
    exp_time = 0.01
    constants_db = VbiConstantsDb(
        NUM_SPATIAL_STEPS=num_steps,
        NUM_DSPS_REPEATS=num_dsps_repeats - (1 * abort_mosaic),  # Freaky
        SPECTRAL_LINE="VBI TEST LINE",
        OBSERVE_EXPOSURE_TIMES=(exp_time,),
    )
    init_vbi_constants_db(recipe_run_id, constants_db)
    with ScienceCalibration(
        recipe_run_id=recipe_run_id,
        workflow_name="vbi_science_calibration",
        workflow_version="VX.Y",
    ) as task:
        task.scratch = WorkflowFileSystem(scratch_base_path=tmp_path, recipe_run_id=recipe_run_id)
        ds = Vbi122ObserveFrames(
            array_shape=(1, 10, 10),
            num_steps=num_steps,
            num_exp_per_step=num_exp_per_step,
            num_dsps_repeats=num_dsps_repeats,
        )
        header_generator = (d.header() for d in ds)
        for s in range(1, num_steps + 1):
            dark_cal = np.zeros((10, 10)) + (s * 10)
            dark_hdul = fits.HDUList([fits.PrimaryHDU(data=dark_cal)])
            task.fits_data_write(
                hdu_list=dark_hdul,
                tags=[
                    VbiTag.intermediate(),
                    VbiTag.frame(),
                    VbiTag.task("DARK"),
                    VbiTag.spatial_step(s),
                    VbiTag.exposure_time(exp_time),
                ],
            )

            # Put in a fake dark just to make sure it doesn't get used
            bad_dark_cal = np.zeros((10, 10)) + (s**2 * 10)
            bad_dark_hdul = fits.HDUList([fits.PrimaryHDU(data=bad_dark_cal)])
            task.fits_data_write(
                hdu_list=bad_dark_hdul,
                tags=[
                    VbiTag.intermediate(),
                    VbiTag.frame(),
                    VbiTag.task("DARK"),
                    VbiTag.spatial_step(s),
                    VbiTag.exposure_time(exp_time**2),
                ],
            )

            gain_cal = np.zeros((10, 10)) + (s + 1)
            gain_hdul = fits.HDUList([fits.PrimaryHDU(data=gain_cal)])
            task.fits_data_write(
                hdu_list=gain_hdul,
                tags=[
                    VbiTag.intermediate(),
                    VbiTag.frame(),
                    VbiTag.task("GAIN"),
                    VbiTag.spatial_step(s),
                ],
            )

            for e in range(num_exp_per_step):
                for d in range(1, num_dsps_repeats + 1):
                    if abort_mosaic and d == num_dsps_repeats and s > num_steps - 2:
                        # Abort the last two mosaic steps of the last DSPS repeat
                        continue
                    header = next(header_generator)
                    data = (np.ones((1, 10, 10)) * (e + 1)) + s + (d * 10)
                    # Multiple by gain
                    data *= gain_cal
                    # Add dark
                    data += dark_cal
                    hdul = generate_214_l0_fits_frame(s122_header=header, data=data)
                    task.fits_data_write(
                        hdu_list=hdul,
                        tags=[
                            VbiTag.input(),
                            VbiTag.task("OBSERVE"),
                            VbiTag.spatial_step(s),
                            VbiTag.dsps_repeat(d),
                            VbiTag.frame(),
                            VbiTag.exposure_time(exp_time),
                        ],
                    )
        if not abort_mosaic:
            ensure_all_inputs_used(header_generator)
        yield task, num_steps, num_exp_per_step, num_dsps_repeats - (1 * abort_mosaic)
        task.scratch.purge()
        task.constants._purge()


@pytest.mark.parametrize(
    "abort_mosaic",
    [pytest.param(False, id="Full set"), pytest.param(True, id="Aborted last mosaic")],
)
def test_science_calibration(science_calibration_task, mocker):
    """
    Given: a set of parsed input observe frames, dark and gain calibrations, and a ScienceCalibration task
    When: the task is run
    Then: the science frames are processed, no exposures are averaged, and the array values are correct
    """
    mocker.patch(
        "dkist_processing_common.tasks.mixin.metadata_store.GraphQLClient", new=FakeGQLClient
    )
    task, num_steps, num_exp_per_step, expected_num_dsps_repeats = science_calibration_task
    task()

    for s in range(1, num_steps + 1):
        tags = [
            VbiTag.calibrated(),
            VbiTag.frame(),
            VbiTag.spatial_step(s),
            VbiTag.stokes("I"),
        ]
        file_list = list(task.read(tags=tags))
        # Make sure any aborted mosaics didn't get processed
        assert len(file_list) == num_exp_per_step * expected_num_dsps_repeats

        for d in range(1, expected_num_dsps_repeats + 1):
            sci_access_list = list(
                task.fits_data_read_fits_access(
                    tags=tags + [VbiTag.dsps_repeat(d)],
                    cls=VbiL0FitsAccess,
                )
            )
            assert len(sci_access_list) == num_exp_per_step
            sorted_access = sorted(sci_access_list, key=lambda x: np.mean(x.data))
            for e, obj in enumerate(sorted_access):
                assert isinstance(obj._hdu, fits.CompImageHDU)
                expected_array = (np.ones((10, 10)) * (e + 1)) + s + (d * 10)
                np.testing.assert_equal(expected_array, obj.data)

    input_obs_frames = list(
        task.read(tags=[VbiTag.input(), VbiTag.frame(), VbiTag.task("OBSERVE")])
    )

    quality_files = list(task.read(tags=[Tag.quality("TASK_TYPES")]))
    for file in quality_files:
        with file.open() as f:
            data = json.load(f)
            assert isinstance(data, dict)
            assert data["total_frames"] == len(input_obs_frames)
