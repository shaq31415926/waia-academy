## ETL Pipeline v1

### Introduction
Building an ETL pipeline that carries out the following tasks:
- Extracts transactional data of 400k invoices from Redshift
- Transforms the data by identifying and removing duplicates
- Loads the transformed data to an s3 bucket

### Requirements
  The minimum requirements:
- Python 3+

### Instructions on how to execute the code
Make sure you are executing the code from the etl_pipeline folder.
1. Install all the libraries you will need to execute main.py.

```
  pip3 install -r requirements.txt
```

2. Copy the ``.env.example`` file to `.env` and fill out the environment vars.

3. Run the main.py script.

```
  python3 main.py
```