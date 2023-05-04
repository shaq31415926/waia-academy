import os
import psycopg2
import pandas as pd
from datetime import datetime
from io import StringIO
import boto3
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator


dbname = os.getenv("dbname")
host = os.getenv("host")
port = os.getenv("port")
user = os.getenv("user")
password = os.getenv("password")
aws_access_key_id = os.getenv("aws_access_key_id")
aws_secret_access_key_id = os.getenv("aws_secret_access_key_id")


def connect_to_redshift():

    connect = psycopg2.connect(
        dbname=dbname, host=host, port=port, user=user, password=password
    )
    print("connection to redshift made")

    return connect


def extract_transactional_data():

    connect = connect_to_redshift()

    query = """select t1.*,
                      case when t2.Description = '?' or t2.Description is null then 'Unknown' 
                        else t2.Description end as Description
                from bootcamp1.online_transactions t1
                left join bootcamp1.stock_description t2 on t1.stock_code = t2.stock_code
                where customer_id <> ''
                    and t1.stock_code not in ('POSTAGE', 'BANK CHARGES', 'D', 'M', 'CRUK')
                    and t1.quantity > 0
               """

    online_transactions_reduced = pd.read_sql(query, connect)

    print(f"The data frame contains {online_transactions_reduced.shape[0]} invoices")

    return online_transactions_reduced

def identify_and_remove_duplicated_data(df):
    """Method that removes identifies and removes duplicates"""

    if df.duplicated().sum() > 0:
        df_cleaned = df.drop_duplicates(keep='first')

        print("-" * 50)
        print("Shape of data before removing duplicates:", df.shape)
        print("Shape of data after removing duplicates:", df_cleaned.shape)
        print("-" * 50)

        return df_cleaned

    else:
        print("no duplicates values found")

        return df

def connect_to_s3(aws_access_key_id, aws_secret_access_key):
    """Methods that connects to s3"""

    s3_client = boto3.client(
        "s3",
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key
    )

    return s3_client


def df_to_s3(df, key, s3_bucket, aws_access_key_id, aws_secret_access_key):
    """Function that writes a data frame as a .csv file to a s3 bucket"""

    csv_buffer = StringIO()  # create buffer to temporarily store the Data Frame

    df.to_csv(csv_buffer, index=False)  # code to write the data frame as csv file

    s3_client = connect_to_s3(aws_access_key_id, aws_secret_access_key)

    s3_client.put_object(
        Bucket=s3_bucket, Key=key, Body=csv_buffer.getvalue()
    )  # this code writes the temp stored csv file and writes to s3

    print(f"The transformed data is saved as CSV in the following location s3://{s3_bucket}/{key}")


def main():
    start_time = datetime.now()

    # extract data
    print("Extracting data")
    ot_data = extract_transactional_data()

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
    key = "online_transactions_transformation/final/sh_online_transactions.csv"  # define the file name

    df_to_s3(ot_data_final, key, aws_s3_bucket, aws_access_key_id, aws_secret_access_key_id)

    execution_time = datetime.now() - start_time
    print(f"\nTotal execution time (hh:mm:ss.ms) {execution_time}")




dag = DAG("etl-pipeline",
          description="Extracts Transforms and Loads Data",
          schedule_interval="@daily",
          start_date=datetime(2023,1,1), catchup=False)

start_dag = DummyOperator(task_id="start_dag", dag=dag)
end_dag = DummyOperator(task_id="end_dag", dag=dag)

etl_operator = PythonOperator(task_id="extract_transform_load_data",
                                  python_callable=main,
                                  dag=dag)

start_dag >> etl_operator >> end_dag