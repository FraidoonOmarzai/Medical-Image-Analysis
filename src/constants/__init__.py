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


# CONSTANS FOR MODET TRAINING 
MODEL_TRAINING_DIR: str = os.path.join(ARTIFACTS_DIR, 'ModelTrainings')
UNZIP_DIR: str = os.path.join(DATA_INGESTION_DIR, IMAGES_DIR)
SAVE_MODEL_NAME: str = 'model.h5'

IMAGE_SIZE: int = (224, 224)
BATCH_SIZE: int = 32
EPOCHS: int = 2


# MLflow CONSTANTS
ARTIFACTS_DIR: str = "mlflow_artifacts"
EXPERIMENT_NAME: str = "medimg_experiment"
RUN_NAME: str = "Transfer_learning_Model"
REGISTERED_MODEL_NAME: str = "EfficientNet"
REMOTE_SERVER_URI: str = "https://dagshub.com/fraidoon_omarzai/Medical-Image-Analysis.mlflow"