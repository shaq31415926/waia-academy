# i am using definitions to do this step, which i will introduce y'all to. Feel free to use the slides.

import boto3
from io import StringIO, BytesIO

def connect_to_s3(aws_access_key_id, aws_secret_access_key):
    """Methods that connects to s3"""

    s3_client = boto3.client(
        "s3",
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key
    )

    print("Connection to s3 made")
    
    return s3_client


def df_to_s3(df, key, s3_bucket, aws_access_key_id, aws_secret_access_key):
    """Function that writes a data frame as a .csv file to a s3 bucket"""
    
    file_type = key[-4:]
    
    if file_type == '.pkl':
        buffer = BytesIO()  # create buffer to temporarily store the Data Frame
        df.to_pickle(buffer)  # code to write the data frame as .pkl file
    
    if file_type == '.csv':
        buffer = StringIO()  # create buffer to temporarily store the Data Frame
        df.to_csv(buffer)  # code to write the data frame as .csv file

    s3_client = connect_to_s3(aws_access_key_id, aws_secret_access_key)

    s3_client.put_object(
        Bucket=s3_bucket, Key=key, Body=buffer.getvalue()
    )  # this code writes the temp stored file and writes to s3


    print(f"The transformed data is saved as CSV in the following location s3://{s3_bucket}/{key}")