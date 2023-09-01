# This script is our first version of building an extract-transform and load pipeline

import os
from src.extract import extract_transactional_data
from src.transform import identify_and_remove_duplicate_data
from src.load_data_to_s3 import df_to_s3

# you need this library to read the passwords when running the code using python
# from dotenv import load_dotenv
# load_dotenv()

# import variables from .env file
dbname = os.getenv("dbname")
host = os.getenv("host")
port = os.getenv("port")
user = os.getenv("user")
password = os.getenv("password")
aws_access_key_id = os.getenv("aws_access_key_id")
aws_secret_access_key_id = os.getenv("aws_secret_access_key_id")

# extracting the data from redshift with some transformations
print("Extracting the data from redshift...")
online_trans_cleaned = extract_transactional_data(dbname, host, port, user, password)

# identifying and remove the duplicates
print("Identifying and removing duplicates...")
online_trans_cleaned = identify_and_remove_duplicate_data(online_trans_cleaned)

# loading the data to s3
print("Loading data to the s3 bucket...")
s3_bucket = "july-bootcamp"
key = "etl_pipeline/docker/sh_online_transactions_v2.pkl"

df_to_s3(online_trans_cleaned, key, s3_bucket, aws_access_key_id, aws_secret_access_key_id)
