from itertools import chain

import pytest
from dkist_processing_common._util.scratch import WorkflowFileSystem
from dkist_processing_common.models.constants import BudName
from dkist_processing_common.tests.conftest import FakeGQLClient

from dkist_processing_vbi.models.constants import VbiBudName
from dkist_processing_vbi.models.tags import VbiTag
from dkist_processing_vbi.tasks.parse import ParseL0VbiInputData
from dkist_processing_vbi.tests.conftest import generate_214_l0_fits_frame
from dkist_processing_vbi.tests.conftest import Vbi122DarkFrames
from dkist_processing_vbi.tests.conftest import Vbi122GainFrames
from dkist_processing_vbi.tests.conftest import Vbi122ObserveFrames


@pytest.fixture(scope="function")
def parse_inputs_task(tmp_path, recipe_run_id, DKIST009_offset):
    with ParseL0VbiInputData(
        recipe_run_id=recipe_run_id,
        workflow_name="vbi_parse_l0_inputs",
        workflow_version="VX.Y",
    ) as task:
        task.scratch = WorkflowFileSystem(scratch_base_path=tmp_path, recipe_run_id=recipe_run_id)
        task.num_program_types = 3
        task.num_steps = 4
        task.num_exp_per_step = 3
        task.test_num_dsps_repeats = 2
        ds1 = Vbi122DarkFrames(
            array_shape=(1, 10, 10),
            num_steps=task.num_steps,
            num_exp_per_step=1,
        )
        ds2 = Vbi122GainFrames(
            array_shape=(1, 10, 10),
            num_steps=task.num_steps,
            num_exp_per_step=1,
        )
        ds3 = Vbi122ObserveFrames(
            array_shape=(1, 10, 10),
            num_steps=task.num_steps,
            num_exp_per_step=task.num_exp_per_step,
            num_dsps_repeats=task.test_num_dsps_repeats,
            DKIST008_value=5280,  # Just a number clearly larger than test_num_dsps_repeats
            DKIST009_offset_value=DKIST009_offset,
        )
        ds = chain(ds1, ds2, ds3)
        header_generator = (d.header() for d in ds)
        for header in header_generator:
            hdul = generate_214_l0_fits_frame(s122_header=header)
            task.fits_data_write(hdu_list=hdul, tags=[VbiTag.input(), VbiTag.frame()])
        yield task
        task.scratch.purge()
        task.constants._purge()


@pytest.fixture(scope="function")
def parse_inputs_task_with_only_observe(tmp_path, recipe_run_id, DKIST009_offset):
    with ParseL0VbiInputData(
        recipe_run_id=recipe_run_id,
        workflow_name="vbi_parse_l0_inputs",
        workflow_version="VX.Y",
    ) as task:
        task.scratch = WorkflowFileSystem(scratch_base_path=tmp_path, recipe_run_id=recipe_run_id)
        task.num_program_types = 3
        task.num_steps = 4
        task.num_exp_per_step = 1
        task.test_num_dsps_repeats = 2
        ds = Vbi122ObserveFrames(
            array_shape=(1, 10, 10),
            num_steps=task.num_steps,
            num_exp_per_step=task.num_exp_per_step,
            num_dsps_repeats=task.test_num_dsps_repeats,
            DKIST008_value=5280,  # Just a number clearly larger than test_num_dsps_repeats
            DKIST009_offset_value=DKIST009_offset,
        )
        header_generator = (d.header() for d in ds)
        for header in header_generator:
            hdul = generate_214_l0_fits_frame(s122_header=header)
            task.fits_data_write(hdu_list=hdul, tags=[VbiTag.input(), VbiTag.frame()])
        yield task
        task.scratch.purge()
        task.constants._purge()


@pytest.fixture(scope="function")
def parse_inputs_task_with_out_of_sequence_DSPSNUMS(tmp_path, recipe_run_id, DKIST009_offset):
    with ParseL0VbiInputData(
        recipe_run_id=recipe_run_id,
        workflow_name="vbi_parse_l0_inputs",
        workflow_version="VX.Y",
    ) as task:
        task.scratch = WorkflowFileSystem(scratch_base_path=tmp_path, recipe_run_id=recipe_run_id)
        task.num_steps = 4
        task.num_exp_per_step = 1
        task.test_num_dsps_repeats = 4
        ds = Vbi122ObserveFrames(
            array_shape=(1, 10, 10),
            num_steps=task.num_steps,
            num_exp_per_step=task.num_exp_per_step,
            num_dsps_repeats=task.test_num_dsps_repeats,
            DKIST008_value=5280,  # Just a number clearly larger than test_num_dsps_repeats
            DKIST009_offset_value=DKIST009_offset,
        )
        header_generator = (d.header() for d in ds)
        for i, header in enumerate(header_generator):
            if header["DKIST009"] == 1003:
                # Skip the 3rd frame (this needs to not be the last one; that would be an aborted last mosaic)
                continue
            hdul = generate_214_l0_fits_frame(s122_header=header)
            task.fits_data_write(hdu_list=hdul, tags=[VbiTag.input(), VbiTag.frame()])
        yield task
        task.scratch.purge()
        task.constants._purge()


@pytest.fixture(scope="function")
def parse_inputs_task_with_aborted_last_mosaic(tmp_path, recipe_run_id, DKIST009_offset):
    num_steps = 4
    num_exp_per_step = 3
    num_dsps_repeats = 4
    with ParseL0VbiInputData(
        recipe_run_id=recipe_run_id,
        workflow_name="vbi_parse_l0_inputs",
        workflow_version="VX.Y",
    ) as task:
        task.scratch = WorkflowFileSystem(scratch_base_path=tmp_path)
        ds = Vbi122ObserveFrames(
            array_shape=(1, 10, 10),
            num_steps=num_steps,
            num_exp_per_step=num_exp_per_step,
            num_dsps_repeats=num_dsps_repeats,
            DKIST008_value=5280,  # Just a number clearly larger than test_num_dsps_repeats
            DKIST009_offset_value=DKIST009_offset,
        )
        header_generator = (d.header() for d in ds)
        for i, header in enumerate(header_generator):
            if header["DKIST009"] == 1004 and header["VBI__004"] > num_steps - 2:
                # Skip the last 2 mosaic steps of the last repeat
                continue
            hdul = generate_214_l0_fits_frame(s122_header=header)
            task.fits_data_write(hdu_list=hdul, tags=[VbiTag.input(), VbiTag.frame()])
        yield task, num_dsps_repeats - 1
        task.scratch.purge()
        task.constants._purge()


def test_parse_l0_input_data_spatial_pos(parse_inputs_task, mocker):
    """
    Given: a set of raw inputs of multiple task types and a ParseL0VbiInputData task
    When: the task is run
    Then: the input frames are correctly tagged by spatial position
    """
    mocker.patch(
        "dkist_processing_common.tasks.mixin.metadata_store.GraphQLClient", new=FakeGQLClient
    )
    parse_inputs_task()

    for step in range(1, parse_inputs_task.num_steps + 1):
        translated_files = list(
            parse_inputs_task.read(tags=[VbiTag.input(), VbiTag.frame(), VbiTag.spatial_step(step)])
        )
        assert (
            len(translated_files)
            == (parse_inputs_task.num_program_types - 1)  # for non observe frames
            + parse_inputs_task.num_exp_per_step
            * parse_inputs_task.constants.num_dsps_repeats  # for observe frames
        )
        for filepath in translated_files:
            assert filepath.exists()


def test_parse_l0_input_constants(parse_inputs_task, mocker, DKIST009_offset):
    """
    Given: a set of raw inputs of multiple task types and a ParseL0VbiInputData task
    When: the task is run
    Then: pipeline constants are correctly updated from the input headers
    """
    mocker.patch(
        "dkist_processing_common.tasks.mixin.metadata_store.GraphQLClient", new=FakeGQLClient
    )
    parse_inputs_task()

    assert (
        parse_inputs_task.constants._db_dict[VbiBudName.num_spatial_steps.value]
        == parse_inputs_task.num_steps
    )
    assert (
        parse_inputs_task.constants._db_dict[BudName.num_dsps_repeats.value]
        == parse_inputs_task.test_num_dsps_repeats
    )
    assert (
        parse_inputs_task.constants._db_dict[VbiBudName.dsps_repeat_pedestal.value]
        == DKIST009_offset
    )
    assert parse_inputs_task.constants._db_dict[BudName.spectral_line.value] == "VBI-Red H-alpha"
    assert (
        parse_inputs_task.constants._db_dict[VbiBudName.num_exp_per_dsp.value]
        == parse_inputs_task.num_exp_per_step
    )


def test_parse_l0_input_frames_found(parse_inputs_task, mocker):
    """
    Given: a set of raw inputs of multiple task types and a ParseL0VbiInputData task
    When: the task is run
    Then: the frames from each task type are correctly identified and tagged
    """
    mocker.patch(
        "dkist_processing_common.tasks.mixin.metadata_store.GraphQLClient", new=FakeGQLClient
    )
    parse_inputs_task()
    assert (
        len(list(parse_inputs_task.read(tags=[VbiTag.input(), VbiTag.task("DARK")])))
        == parse_inputs_task.num_steps
    )
    assert (
        len(list(parse_inputs_task.read(tags=[VbiTag.input(), VbiTag.task("GAIN")])))
        == parse_inputs_task.num_steps
    )

    assert (
        len(list(parse_inputs_task.read(tags=[VbiTag.input(), VbiTag.task("OBSERVE")])))
        == parse_inputs_task.num_steps
        * parse_inputs_task.num_exp_per_step
        * parse_inputs_task.test_num_dsps_repeats
    )


def test_parse_l0_input_with_only_observe(parse_inputs_task_with_only_observe, mocker):
    """
    Given: a set of raw inputs of a single task type and a ParseL0VbiInputData task
    When: the task is run
    Then: the observe frames are correctly identified and tagged
    """
    mocker.patch(
        "dkist_processing_common.tasks.mixin.metadata_store.GraphQLClient", new=FakeGQLClient
    )
    parse_inputs_task_with_only_observe()
    for dsps_repeat in range(1, parse_inputs_task_with_only_observe.test_num_dsps_repeats + 1):
        for step in range(1, parse_inputs_task_with_only_observe.num_steps + 1):
            translated_files = list(
                parse_inputs_task_with_only_observe.read(
                    tags=[
                        VbiTag.input(),
                        VbiTag.frame(),
                        VbiTag.task("OBSERVE"),
                        VbiTag.spatial_step(step),
                        VbiTag.dsps_repeat(dsps_repeat),
                    ]
                )
            )
            assert len(translated_files) == parse_inputs_task_with_only_observe.num_exp_per_step
            for filepath in translated_files:
                assert filepath.exists()


def test_parse_l0_raises_error_on_bad_DSPSNUM_sequence(
    parse_inputs_task_with_out_of_sequence_DSPSNUMS, mocker
):
    """
    Given: a set of observe frames that are missing a DSPSNUM
    When: parsing the frames
    Then: an error is raised
    """
    mocker.patch(
        "dkist_processing_common.tasks.mixin.metadata_store.GraphQLClient", new=FakeGQLClient
    )
    with pytest.raises(ValueError, match="Set of DSPS nums is not equal"):
        parse_inputs_task_with_out_of_sequence_DSPSNUMS()


def test_parse_l0_aborted_last_mosaic(parse_inputs_task_with_aborted_last_mosaic, mocker):
    """
    Given: a set of raw inputs representing a dataset with an aborted last mosaic
    When: the task is run
    Then: pipeline constants are correctly updated from the input headers
    """
    mocker.patch(
        "dkist_processing_common.tasks.mixin.metadata_store.GraphQLClient", new=FakeGQLClient
    )
    task, expected_num_dsps_repeats = parse_inputs_task_with_aborted_last_mosaic
    task()

    assert task.constants._db_dict[BudName.num_dsps_repeats.value] == expected_num_dsps_repeats
