import psycopg2
import boto3
from io import StringIO


def connect_to_redshift(dbname, host, port, user, password):
    """connect to redshift"""

    connect = psycopg2.connect(
            dbname=dbname, host=host, port=port, user=user, password=password
        )

    cursor = connect.cursor()
    
    print("connection to redshift made")
    
    return connect, cursor


def connect_to_s3(aws_access_key_id, aws_secret_access_key):
    """connect to s3"""
    
    s3_client = boto3.client(
    "s3",
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)
    
     return s3_client
    

def df_to_s3(df, key, s3_bucket):
    """Function that writes a data frame as a .csv file to an s3 bucket"""

    csv_buffer = StringIO() # create buffer to temporarily store the Data Frame

    df.to_csv(csv_buffer, index=False) # code to write the data frame as csv file
    
    s3_client = connect_to_s3(aws_access_key_id, aws_secret_access_key)
    
    response = s3_client.put_object(
            Bucket=s3_bucket, Key=key, Body=csv_buffer.getvalue()
        ) # this code writes the temp stored csv file and writes to s3

    print("Dataframe is saved as CSV in S3 bucket.") # prints a statement to let us know the file has been written