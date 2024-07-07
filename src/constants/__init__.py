import os

# COMMON CONSTANTS
ARTIFACTS_DIR: str = os.path.join('artifacts')
BUCKET_NAME: str = 'rsnadataset'
S3_DATA_FOLDER: str = 'data' # bucket folder name
S3_FILE: str = 'RSNA.zip'


# CONSTANTS FOR DATA INGESTIONS
DATA_INGESTION_DIR: str = os.path.join(ARTIFACTS_DIR, 'DataIngestion')
IMAGES_DIR: str = "images"


# CONSTANTS FOR DATA VALIDATION
DATA_VALIDATION_DIR: str = os.path.join(ARTIFACTS_DIR, 'DataValidation')
IMG_STATUS_FILE: str = 'img_status.txt'