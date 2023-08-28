import os
# you are importing the function called connect_to_redshift from the extract script
from src.extract import connect_to_redshift

# you need this library to read the passwords
from dotenv import load_dotenv
load_dotenv()

# import variables from .env file
dbname = os.getenv("dbname")
host = os.getenv("host")
port = os.getenv("port")
user = os.getenv("user")
password = os.getenv("password")
aws_access_key_id = os.getenv("aws_access_key_id")
aws_secret_access_key_id = os.getenv("aws_secret_access_key_id")

# make a connection to redshift
connect_to_redshift(dbname, host, port, user, password)