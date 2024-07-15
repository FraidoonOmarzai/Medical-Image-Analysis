from dataclasses import dataclass


@dataclass
class DataIngestionArtifacts:
    RSNA_DATA_PATH: str


@dataclass
class DataValidationArtifacts:
    IMG_STATUS_FILE_PATH: str


@dataclass
class ModelTrainingArtifacts:
    MODEL_TRAINED_PATH: str


@dataclass
class LogProductionModelArtifacts:
    BEST_MODEL_PATH: str


@dataclass
class ModelPusherArtifacts:
    BUCKET_NAME: str
