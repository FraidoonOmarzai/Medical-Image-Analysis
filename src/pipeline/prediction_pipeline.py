from src.logger import logging
from src.exception import CustomException
from src.cloud_storage.s3_operations import S3Operation
from src.constants import *

import os
import sys


class PredictionPipeline:
    """A class for running prediction pipeline using a trained model.

    Attributes:
        bucket_name (str): The name of the S3 bucket where the best model is stored.
        bucket_folder_name (str): The directory path within the S3 bucket where the best model is located.
        model_name (str): The name of the best model file.
        pred_model_path (str): The local directory path where the best model will be downloaded.
        s3_operation (S3Operation): An instance of the S3Operation class for interacting with S3.

    Methods:
        get_model_from_s3(): Download the best model from S3 and return the local path.
        run_pipeline(): Run the prediction pipeline on the provided and ruturn the path to best model.

    """

    def __init__(self):
        self.bucket_name = BUCKET_NAME
        self.bucket_folder_name = S3_MODEL_FOLDER
        self.model_name = BEST_MODEL_NAME
        self.pred_model_path = os.path.join("artifacts", "PredictModel")
        self.s3_operation = S3Operation()

    def get_model_from_s3(self) -> str:
        try:
            logging.info("Loading the best model from s3 bucket")
            os.makedirs(self.pred_model_path, exist_ok=True)
            self.s3_operation.sync_folder_from_s3(self.pred_model_path,
                                                  self.bucket_name,
                                                  self.bucket_folder_name)

            best_model_path = os.path.join(
                self.pred_model_path, self.model_name)
            logging.info("Best model downloaded from s3 bucket")
            return best_model_path

        except Exception as e:
            raise CustomException(e, sys)

    def run_pipeline(self):
        try:
            logging.info("Running prediction pipeline")
            if not os.path.exists(os.path.join(self.pred_model_path, self.model_name)):
                best_model_path: str = self.get_model_from_s3()

                return best_model_path

            best_model_path = os.path.join(
                self.pred_model_path, self.model_name)
            return best_model_path

        except Exception as e:
            raise CustomException(e, sys)
