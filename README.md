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

    