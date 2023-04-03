import os
from src.extract import extract_transactional_data

from dotenv import load_dotenv
load_dotenv() # only for local testing


# import variables from .env file
dbname = os.getenv("dbname")
host = os.getenv("host")
port = os.getenv("port")
user = os.getenv("user")
password = os.getenv("password")
aws_access_key_id = os.getenv("aws_access_key_id")
aws_secret_access_key_id = os.getenv("aws_secret_access_key_id")


# extract data
ot_data = extract_transactional_data(dbname, host, port, user, password)