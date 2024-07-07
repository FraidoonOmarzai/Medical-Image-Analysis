from src.exception import CustomException
from src.logger import logging
from src.entity.config_entity import DataValidationConfig
from src.entity.artifact_entity import DataValidationArtifacts
from src.components.data_validation import DataValidation

import sys


class DataValidationPipeline:
    """Class representing a data validation pipeline.

    Methods:
        start_data_validation: Starts the data validation process.
        run_pipeline: Runs the pipeline.
    """

    def __init__(self):
        self.data_validation_config = DataValidationConfig()

    def start_data_validation(self):
        try:
            logging.info("Starting data validation pipeline...")

            data_validation = DataValidation(self.data_validation_config)
            data_validation_artifacts = data_validation.init_data_validation()
            return data_validation_artifacts
        except Exception as e:
            raise CustomException(e, sys)

    def run_pipeline(self):
        data_validation_artifacts: DataValidationArtifacts = self.start_data_validation()
        logging.info("Data validation pipeline done...")


if __name__ == '__main__':
    try:
        data_validation_pipeline = DataValidationPipeline()
        data_validation_pipeline.run_pipeline()
    except Exception as e:
        raise CustomException(e, sys)
