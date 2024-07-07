from src.exception import CustomException
from src.logger import logging
from src.entity.config_entity import DataValidationConfig
from src.entity.artifact_entity import DataValidationArtifacts

from PIL import Image
from pathlib import Path
import sys
import os


class DataValidation:
    def __init__(self, data_validation_config: DataValidationConfig):
        self.data_validation_config = data_validation_config

    def check_image_format(self, directory, valid_formats=None):
        """
        Check the format of image files in a directory.

        Parameters:
        - directory: Path to the directory containing image files.
        - valid_formats: A list of valid image formats (e.g., ['JPEG', 'PNG']). If None, defaults to common formats.

        Returns:
        - A list of files with invalid formats.
        """

        try:
            logging.info("Checking image format...")

            if valid_formats is None:
                valid_formats = ['JPEG']

            invalid_files = []

            for filename in os.listdir(directory):
                filepath = os.path.join(directory, filename)
                # used to check if a given path is a file, to ensure that you're only processing files and not directories
                if os.path.isfile(filepath):
                    try:
                        with Image.open(filepath) as img:
                            if img.format not in valid_formats:
                                invalid_files.append(filename)
                    except (IOError, SyntaxError) as e:
                        invalid_files.append(filename)

            return invalid_files
        except Exception as e:
            raise CustomException(e, sys)

    def init_data_validation(self):
        try:
            logging.info('init_data_validation...')
            directory_path = self.data_validation_config.IMAGE_DIR_PATH
            invalid_images = self.check_image_format(directory_path)

            os.makedirs(
                self.data_validation_config.DATA_VALIDATION_PATH, exist_ok=True)
            if invalid_images:
                logging.info('Invalid image files')
                with open(self.data_validation_config.IMG_STATUS_FILE_PATH, 'w') as f:
                    f.write(f"Invalid image files: {invalid_images}")
            else:
                logging.info('All images are in valid formats.')
                with open(self.data_validation_config.IMG_STATUS_FILE_PATH, 'w') as f:
                    f.write("All images are in valid formats.")

            data_validation_artifacts = DataValidationArtifacts(
                IMG_STATUS_FILE_PATH=self.data_validation_config.IMG_STATUS_FILE_PATH
            )

            return data_validation_artifacts

        except Exception as e:
            raise CustomException(e, sys)
