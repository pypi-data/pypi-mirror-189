"""VBI gain task."""
import logging

import numpy as np
from astropy.io import fits
from dkist_processing_common.tasks.mixin.fits import FitsDataMixin
from dkist_processing_common.tasks.mixin.quality import QualityMixin
from dkist_processing_math.arithmetic import subtract_array_from_arrays
from dkist_processing_math.statistics import average_numpy_arrays

from dkist_processing_vbi.models.tags import VbiTag
from dkist_processing_vbi.parsers.vbi_l0_fits_access import VbiL0FitsAccess
from dkist_processing_vbi.tasks.mixin.intermediate_loaders import IntermediateLoaderMixin
from dkist_processing_vbi.tasks.vbi_base import VbiTaskBase


class GainCalibration(VbiTaskBase, FitsDataMixin, IntermediateLoaderMixin, QualityMixin):
    """
    Task class for calculation of a single gain frame for each spatial position. (Note that VBI only ever deals with Solar Gain frames).

    Parameters
    ----------
    recipe_run_id : int
        id of the recipe run used to identify the workflow run this task is part of
    workflow_name : str
        name of the workflow to which this instance of the task belongs
    workflow_version : str
        version of the workflow to which this instance of the task belongs
    """

    record_provenance = True

    def run(self) -> None:
        """
        For each spatial step.

            - Gather input solar gain frames
            - Calculate average gain
            - Write average gain
            - Record quality metrics

        Returns
        -------
        None

        """
        # These will be running totals used to save a pass when computing the full-FOV normalization
        self.total_counts: float = 0.0
        self.total_non_nan_pix: int = 0

        # We'll just stuff the un-normalized arrays in this dictionary to avoid dealing with tags, io, etc.
        # This is OK (tm) because this will be, at most, 9 4k x 4k arrays. This is a lot (~1G), but not too much.
        step_gain_dict: dict = {}

        with self.apm_processing_step(
            f"Collecting and reducing gain arrays from {self.constants.num_spatial_steps} steps and {len(self.constants.gain_exposure_times)} exp times",
        ):
            for exp_time in self.constants.gain_exposure_times:
                for step in range(1, self.constants.num_spatial_steps + 1):
                    logging.info(f"retrieving dark frame step {step} and {exp_time = }")
                    try:
                        dark_calibration_array = self.intermediate_dark_array(
                            spatial_step=step, exposure_time=exp_time
                        )
                    except StopIteration:
                        raise ValueError(f"No matching dark found for {exp_time = }")

                    logging.info(f"collecting gain frames for {step = }")
                    input_gain_access = self.fits_data_read_fits_access(
                        tags=[
                            VbiTag.input(),
                            VbiTag.frame(),
                            VbiTag.spatial_step(step),
                            VbiTag.task("GAIN"),
                            VbiTag.exposure_time(exp_time),
                        ],
                        cls=VbiL0FitsAccess,
                    )
                    input_gain_arrays = (obj.data for obj in input_gain_access)

                    logging.info(f"averaging arrays from {step = }")
                    averaged_gain_array = average_numpy_arrays(input_gain_arrays)
                    logging.info(
                        f"average raw gain signal in step {step} = {averaged_gain_array.mean():.3e}"
                    )

                    logging.info(f"subtracting dark from average gain for {step = }")
                    dark_subtracted_gain_array = next(
                        subtract_array_from_arrays(
                            arrays=averaged_gain_array, array_to_subtract=dark_calibration_array
                        )
                    )

                    logging.info(f"Recording processed gain image for {step = }")
                    self.total_non_nan_pix += np.sum(~np.isnan(dark_subtracted_gain_array))
                    self.total_counts += np.nansum(dark_subtracted_gain_array)
                    step_gain_dict[step] = dark_subtracted_gain_array

        with self.apm_processing_step("normalizing gain arrays"):
            normalized_array_dict = self.normalize_fov(step_gain_dict)

        with self.apm_writing_step("writing gain arrays to disk"):
            self.write_gain_calibration(normalized_array_dict)

        with self.apm_processing_step("Computing and logging quality metrics"):
            no_of_raw_gain_frames: int = self.count(
                tags=[
                    VbiTag.input(),
                    VbiTag.frame(),
                    VbiTag.task("GAIN"),
                ],
            )
            self.quality_store_task_type_counts(
                task_type="gain", total_frames=no_of_raw_gain_frames
            )

    def normalize_fov(self, step_gain_dict: dict[int, np.ndarray]) -> dict[int, np.ndarray]:
        """
        Find the global mean of the entire FOV and divide each frame (each spatial step) by this mean.

        Parameters
        ----------
        step_gain_dict : Dict
            Dictionary of dark subtracted gain array for each spatial step

        Returns
        -------
        Dict
            Dict of FOV normalized gain arrays
        """
        fov_mean = self.total_counts / self.total_non_nan_pix
        logging.info(f"full FOV mean = {fov_mean:.3e}")
        for k in step_gain_dict:
            step_gain_dict[k] = step_gain_dict[k] / fov_mean

        return step_gain_dict

    def write_gain_calibration(self, gain_array_dict: dict[int, np.ndarray]) -> None:
        """
        Apply correct tags to each spatial step and write to disk.

        Parameters
        ----------
        gain_array_dict : Dict
            Dictionary of corrected gain arrays

        Returns
        -------
        None
        """
        for step, data in gain_array_dict.items():
            hdul = fits.HDUList([fits.PrimaryHDU(data=data)])
            self.fits_data_write(
                hdu_list=hdul,
                tags=[
                    VbiTag.intermediate(),
                    VbiTag.frame(),
                    VbiTag.task("GAIN"),
                    VbiTag.spatial_step(step),
                ],
            )
