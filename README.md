<h1 align=center> Medical-Image-Analysis </h1>

**Implementing end-to-end deep learning project, and using MLOps tools**

- Git clone the repository and define the template of the project
```bash
git clone https://github.com/-----
touch template.py
python template.py
```
- define setup.py file

- install the new env and requirements.txt

```bash
conda create -n medimg python=3.9 -y
conda activate medimg
pip install -r requirements.txt
```
- define the logger

- define the exception handler

- **experiments in google colabs**
    - download the dataset to google colabs
    - EDA
    - perform feature engineering
        - converting dicom file to jpeg format
        - prepare the dataset for training
        - create sample data of 400 images for training and 200 images for validating
        - download the sample data to local disk and store it in S3
    - train the model on the entire dataset
        - using transfer learning and fine tuning
    - model evaluation
    - `note` we used the notebook in google colabs for experiment purposes and creating sample data for training and validating.

```bash
## Workflows
- update the constants
- updata the artifact_entity
- update the config_entity
- update the components
- update the pipeline
- update the dvc.yaml (optional)
```

- **S3 Storage**
    - add s3_operations.py for uploading and downloading files to/from s3 bucket
    - we need to run the below command which allows to configure AWS credentials and settings
    ```bash
    aws configure  
    ```
    - our goal is to store the sample data in s3 bucket which we created in google colabs

- **Data Ingestion**
    - get the data from the bucket and save it in artifacts/data_ingestion
    - follow the above workflows to get the data from the S3 bucket


- **Data Validations**
    - we are going to verify the file format
    - `file_format = ["JPEG"]`

- **Model Training**
    - model training and evaluation 
    - follow the above workflows
    - add the model architecture to model/model.py
    - save the model 

- **Adding MLflow**
    - add MLflow for managing ML experiments, track metrics and parameters, and compare different model iterations
    - using `Dagshub`
    - env variables
    ```bash
    export MLFLOW_TRACKING_URI='https://dagshub.com/fraidoon_omarzai/Medical-Image-Analysis.mlflow'
    export MLFLOW_TRACKING_USERNAME='fraidoon_omarzai' 
    export MLFLOW_TRACKING_PASSWORD='bc....'
    ```
    - create `.env` and store the dagshub tocken on it
    ```bash
    from dotenv import load_dotenv
    load_dotenv() 
    
    os.environ["MLFLOW_TRACKING_URI"]="https://dagshub.com/fraidoon_omarzai/Medical-Image-Analysis.mlflow"
    os.environ["MLFLOW_TRACKING_USERNAME"]="fraidoon_omarzai"
    os.environ["MLFLOW_TRACKING_PASSWORD"]=os.getenv('DAGSHUB_TOKEN')
    ```

- **log production model**
    - we are going to load all models from dagshub using MLflow
    - transitions the model to stage (from none, to staging, to production) 
    - best model to "Production" stage and rest to "Staging" stage
    - store the best model in S3 bucket
