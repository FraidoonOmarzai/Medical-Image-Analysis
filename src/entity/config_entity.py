from src.constants import *
import os


class DataIngestionConfig:
    """Data class for configuring data ingestion parameters.

    This class provides a convenient way to configure parameters related to data ingestion,
    such as directory paths and S3 bucket names.

    args:

    """

    def __init__(self) -> None:
        self.S3_DATA_FOLDER = S3_DATA_FOLDER
        self.BUCKET_NAME = BUCKET_NAME
        self.S3_FILE = S3_FILE

        self.DATA_INDESTION_PATH = os.path.join(DATA_INGESTION_DIR)

        self.ZIP_PATH = os.path.join(self.DATA_INDESTION_PATH, S3_FILE)
        self.UNZIP_PATH = os.path.join(self.DATA_INDESTION_PATH, IMAGES_DIR)


class DataValidationConfig:
    """A class for configuring data validation parameters.

    This class provides a convenient way to configure parameters related to data validation,
    such as directory paths and img_status.txt file.

    """

    def __init__(self) -> None:
        self.DATA_VALIDATION_PATH = os.path.join(DATA_VALIDATION_DIR)
        self.IMAGE_DIR_PATH = os.path.join(DATA_INGESTION_DIR, IMAGES_DIR)
        self.IMG_STATUS_FILE_PATH = os.path.join(
            self.DATA_VALIDATION_PATH, IMG_STATUS_FILE)
