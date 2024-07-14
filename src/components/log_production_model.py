import warnings
from src.exception import CustomException
from src.logger import logging
from src.entity.artifact_entity import LogProductionModelArtifacts
from src.entity.config_entity import LogProductionModelConfig
from src.constants import *

import mlflow
from mlflow.tracking import MlflowClient
from pprint import pprint
import tensorflow as tf
import sys

from dotenv import load_dotenv
load_dotenv()

warnings.filterwarnings("ignore")


class LogProductionModel:
    """A class for Log Production models.
    This class facilitates the process of getting the best model from dagshub using mlflwo, 
    registering models in stagging and production stage, and save the best model in S3.    
    Attributes:
        - log_model_prod_config (LogProductionModelConfig): Configuration parameters.

    Methods:
        - log_production()
        - init_log_production_model()
    """

    def __init__(self, log_model_prod_config: LogProductionModelConfig):
        self.log_model_prod_config = log_model_prod_config

    def log_production(self):
        try:
            logging.info("log production model section ...")

            os.environ["MLFLOW_TRACKING_URI"] = REMOTE_SERVER_URI
            os.environ["MLFLOW_TRACKING_USERNAME"] = "fraidoon_omarzai"
            os.environ["MLFLOW_TRACKING_PASSWORD"] = os.getenv('DAGSHUB_TOKEN')

            mlflow.set_tracking_uri(REMOTE_SERVER_URI)

            # Specify the name of the experiment
            experiment_name = "medimgExperiments"
            experiment = mlflow.get_experiment_by_name(experiment_name)
            experiment_id = experiment.experiment_id
            logging.info(f'experiment_id: {experiment_id}')

            # Query the best run based on a specific metric (e.g., 'accuracy')
            best_run = mlflow.search_runs(
                experiment_ids=[experiment_id],
                order_by=["metrics.val_accuracy DESC"],  # best val_accuracy
                max_results=1
            )
            best_run_id = best_run.iloc[0].run_id
            logging.info(f'best_run_id: {best_run_id}')

            # load the best model with highest val_accuracy
            model_uri = f"runs:/{best_run_id}/mlflow_model.keras"
            model = mlflow.tensorflow.load_model(model_uri)
            # save the model
            os.makedirs(
                self.log_model_prod_config.LOG_PROD_MODEL_DIR, exist_ok=True)
            model.save(self.log_model_prod_config.BEST_MODEL_PATH)
            logging.info("model saved!")

            # from None, to Staging, to Production
            logging.info('model stagging...')
            model_name = REGISTERED_MODEL_NAME
            client = MlflowClient()
            for mv in client.search_model_versions(f"name='{model_name}'"):
                mv = dict(mv)

                if mv["run_id"] == best_run_id:
                    current_version = mv["version"]
                    logged_model = mv["source"]
                    run_id = mv["run_id"]
                    pprint(mv, indent=4)
                    client.transition_model_version_stage(
                        name=model_name,
                        version=current_version,
                        stage="Production"
                    )
                else:
                    current_version = mv["version"]
                    client.transition_model_version_stage(
                        name=model_name,
                        version=current_version,
                        stage="Staging"
                    )
        except Exception as e:
            raise CustomException(e, sys)

    def init_log_production_model(self):
        try:
            self.log_production()

            log_production_model_artificats = LogProductionModelArtifacts(
                self.log_model_prod_config.BEST_MODEL_PATH
            )
            return log_production_model_artificats
        except Exception as e:
            raise CustomException(e, sys)
