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

- **model pusher**    
    - store the best model in S3 bucket


- Add everything to train_pipeline
    - create src\pipeline\train_pipeline.py
    - add code to demo.py
    - run python demo.py


- **streamlit and prediction pipeline**
    - create an application using streamlit -> `app.y`
    - create prediction pipeline, it will download the best model from s3 -> `prediction_pipeline.py`


- **Docker file**
    - create Dockerfile
    - built a docker images
    ```bash
    docker build -t medimg-app .
    docker ps
    docker images
    ```
    - running our app
    ```bash
    docker run -p 8080:8080 medimg-app
    ```
    - finally, open the browser and run:
    ```bash
    htpp://localhost:8080
    ```

- **CI/CD (GithubAction)**
    - create `.github/workflows/docker.yaml`
    - add code to `docker.yaml`
    - build and push to docker hub

#####################**AWS Section**#####################

```bash
# Description about the deployment:
1. Build docker image of the source code
2. Push your docker image to ECR
3. Launch Your EC2 
4. Pull Your image from ECR in EC2
5. Lauch your docker image in EC2


# Notes
ECR: Elastic Container registry to save your docker image in AWS
EC2: It is virtual machine
```

### Steps:

1. Login to AWS console and create IAM user for deployment. Download the access key.
```bash
# Policy for IAM:
1. AmazonEC2ContainerRegistryFullAccess
2. AmazonEC2FullAccess
```

2. Create ECR repo to store/save docker image
```bash
Save the URI: 851725628730.dkr.ecr.eu-west-2.amazonaws.com/medimg
```
3. Create EC2 machine (Ubuntu)
4. Open EC2 and Install docker in EC2 Machine
```bash
#optinal
sudo apt-get update
sudo apt-get upgrade -y

#required
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
```

5. Configure EC2 as self-hosted runner
```bash
1. open your github repository
2. go to the setting
3. find the actions -> runner
4. new self hosted runner -> choose os
5. copy each command and run it on EC2 Instance Connect
```

6. Setup github secrets
```bash
AWS_ACCESS_KEY_ID=...
AWS_SECRET_ACCESS_KEY=...
AWS_REGION = eu-west-2
AWS_ECR_LOGIN_URI =  851725628730.dkr.ecr.eu-west-2.amazonaws.com
ECR_REPOSITORY_NAME = medimg
```