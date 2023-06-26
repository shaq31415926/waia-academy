import os
from datetime import datetime
from src.extract import extract_transactional_data
from src.transform import identify_and_remove_duplicated_data
from src.load_to_s3 import df_to_s3

# only for running the code from command line
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

# this creates a variable that tracks the time we executed the script
start_time = datetime.now()

# make a connection to redshift and extract transactional data with transformation tasks
print("Extracting and transforming data in sql")
online_trans_cleaned = extract_transactional_data(dbname, host, port, user, password)

# next step, deduplicate the data...
print("Removing duplicated data")
online_trans_deduped = identify_and_remove_duplicated_data(online_trans_cleaned)

# next step, load the deduped data to s3
print("Loading data to s3")
s3_bucket = "waia-data-dump"
# the key should include your initial
key = "bootcamp2/etl/sh_online_trans_cleaned.csv"

df_to_s3(online_trans_deduped,
         key,
         s3_bucket,
         aws_access_key_id,
         aws_secret_access_key_id)

# this creates a variable that calculates how long it takes to run the script
execution_time = datetime.now() - start_time
print(f"\nTotal execution time (hh:mm:ss.ms) {execution_time}")