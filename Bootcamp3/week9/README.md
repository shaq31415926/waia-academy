## ETL Pipeline v1

### Introduction
Building an ETL pipeline that carries out the following tasks:
- Extracts transactional data of 400k invoices from Redshift with cleaning as identified during the [data quality audit]()
- Transforms the data by identifying and removing duplicates
- Loads the transformed data to a s3 bucket

---

### Requirements
  The minimum requirements:
- Python 3+

I executed this code with Python 3.11 and the libraries versions are listed in the [requirements file](https://github.com/shaq31415926/waia-academy/blob/main/Bootcamp3/week9/requirements.txt).

### Instructions on how to execute the code
Make sure you are executing the code from the same location as the `main.py` script.

1. Install all the libraries you will need to execute `main.py`. 

```
  pip3 install -r requirements.txt
```

2. Copy the `.env.example` file to `.env` and fill out the environment variables.

3. Run the main.py script, which carries out the extraction-transformation and load tasks.

```
  python3 main.py
```