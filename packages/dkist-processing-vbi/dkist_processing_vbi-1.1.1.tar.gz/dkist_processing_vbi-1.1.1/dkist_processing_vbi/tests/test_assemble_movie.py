import numpy as np
import pytest
from dkist_processing_common._util.scratch import WorkflowFileSystem
from dkist_processing_common.tests.conftest import FakeGQLClient

from dkist_processing_vbi.models.tags import VbiTag
from dkist_processing_vbi.tasks.assemble_movie import AssembleVbiMovie
from dkist_processing_vbi.tests.conftest import generate_214_l1_fits_frame
from dkist_processing_vbi.tests.conftest import Vbi122ObserveFrames
from dkist_processing_vbi.tests.conftest import VbiConstantsDb


@pytest.fixture(scope="function")
def assemble_task_with_tagged_movie_frames(tmp_path, recipe_run_id, init_vbi_constants_db):
    num_dsps_repeats = 10
    constants_db = VbiConstantsDb(NUM_DSPS_REPEATS=num_dsps_repeats)
    init_vbi_constants_db(recipe_run_id, constants_db)
    with AssembleVbiMovie(
        recipe_run_id=recipe_run_id, workflow_name="vbi_make_movie_frames", workflow_version="VX.Y"
    ) as task:
        task.scratch = WorkflowFileSystem(scratch_base_path=tmp_path, recipe_run_id=recipe_run_id)
        task.testing_num_dsps_repeats = num_dsps_repeats
        task.num_steps = 1
        task.num_exp_per_step = 1
        ds = Vbi122ObserveFrames(
            array_shape=(1, 100, 100),
            num_steps=task.num_steps,
            num_exp_per_step=task.num_exp_per_step,
            num_dsps_repeats=task.testing_num_dsps_repeats,
        )
        header_generator = (d.header() for d in ds)
        for d, header in enumerate(header_generator):
            data = np.ones((100, 100))
            data[: d * 10, :] = 0.0
            hdl = generate_214_l1_fits_frame(data=data, s122_header=header)
            hdl[1].header["DSPSNUM"] = d + 1
            task.fits_data_write(
                hdu_list=hdl,
                tags=[
                    VbiTag.movie_frame(),
                    VbiTag.dsps_repeat(d + 1),
                ],
            )
        yield task
        task.scratch.purge()
        task.constants._purge()


def test_assemble_movie(assemble_task_with_tagged_movie_frames, mocker):
    mocker.patch(
        "dkist_processing_common.tasks.mixin.metadata_store.GraphQLClient", new=FakeGQLClient
    )
    assemble_task_with_tagged_movie_frames()
    movie_file = list(assemble_task_with_tagged_movie_frames.read(tags=[VbiTag.movie()]))
    assert len(movie_file) == 1
    assert movie_file[0].exists()
    # import os
    # os.system(f"cp {movie_file[0]} foo.mp4")
