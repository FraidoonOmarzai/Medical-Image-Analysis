from dataclasses import dataclass 


@dataclass
class DataIngestionArtifacts:
    RSNA_DATA_PATH: str
    
    
@dataclass
class DataValidationArtifacts:
    IMG_STATUS_FILE_PATH: str    