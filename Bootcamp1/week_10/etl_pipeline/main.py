import os
import pandas as pd
from src.extract import extract_transactional_data
from src.transform import identify_and_remove_duplicated_data
from src.load_data_to_s3 import df_to_s3

from datetime import datetime

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


def main():
    start_time = datetime.now()

    # extract data
    print("Extracting data")
    ot_data = extract_transactional_data(dbname, host, port, user, password)

    # transform data
    print("Transforming data - removing duplicates")
    # remove duplicates
    ot_data_cleaned = identify_and_remove_duplicated_data(ot_data)

    # fix the invoice date
    print("Transforming data - fixing date time")
    ot_data_final = ot_data_cleaned.copy()
    ot_data_final['invoice_date'] = pd.to_datetime(ot_data_final['invoice_date'])

    # load data to s3
    print("Loading data")
    aws_s3_bucket = "waia-data-dump"  # define the s3 bucket
    dt = datetime.now().strftime("%Y%m%d_%H%M%S")
    key = f"online_transactions_transformation/final/sh_online_transactions_{dt}.csv"  # define the file name

    df_to_s3(ot_data_final, key, aws_s3_bucket, aws_access_key_id, aws_secret_access_key_id)

    execution_time = datetime.now() - start_time
    print(f"\nTotal execution time (hh:mm:ss.ms) {execution_time}")


if __name__ == "__main__":
    main()
