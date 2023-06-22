# This code will not work for students :(

import os
import pandas as pd
from load_to_s3 import connect_to_s3
from extract import connect_to_redshift

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

s3_bucket = "waia-data-dump"
key = "bootcamp2/etl/sh_online_trans_cleaned.csv"

# load this file to redshift
# read the s3 file and store as a data frame
s3_client = connect_to_s3(aws_access_key_id, aws_secret_access_key_id)
response = s3_client.get_object(Bucket=s3_bucket, Key=key)
cleaned_data = pd.read_csv(response.get("Body"))
print(cleaned_data.shape)

# create table in redshift
# connect to redshift
connect = connect_to_redshift(dbname, host, port, user, password)
cursor = connect.cursor()

table_destination = "bootcamp.online_transactions_cleaned"

# create the table in sql
query = f"""
CREATE TABLE {table_destination} ( 
            invoice VARCHAR(7),
            stock_code VARCHAR(12),
            description VARCHAR(42),
            price FLOAT8,
            quantity INT4,
            total_order_value FLOAT8,
            invoice_date DATETIME,
            customer_id VARCHAR(6),
            country VARCHAR(20))
            ;
"""


cursor.execute(query)


def load_from_s3_to_redshift(dbname, host, port, user, password,
                             table_destination, s3_bucket, key, aws_access_key_id,
                             aws_secret_access_key_id):
    query = f"""
        COPY
        {table_destination}
        FROM
        's3://{s3_bucket}/{key}'
        with credentials
            'aws_access_key_id={aws_access_key_id};aws_secret_access_key={aws_secret_access_key_id}'
        FORMAT AS CSV
        IGNOREHEADER 1
        ;"""

    cursor.execute(query)
    connect.commit()

# load the data from s3 to redshift
load_from_s3_to_redshift(dbname, host, port, user, password,
                         table_destination, s3_bucket, key, aws_access_key_id,
                         aws_secret_access_key_id)
print("The data is loaded to redshift")