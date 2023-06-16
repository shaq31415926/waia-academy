import os
from src.extract import connect_to_redshift

from dotenv import load_dotenv
load_dotenv()  # only for local testing

# import variables from .env file
dbname = os.getenv("dbname")
host = os.getenv("host")
port = os.getenv("port")
user = os.getenv("user")
password = os.getenv("password")
aws_access_key_id = os.getenv("aws_access_key_id")
aws_secret_access_key_id = os.getenv("aws_secret_access_key_id")

connect_to_redshift(dbname, host, port, user, password)