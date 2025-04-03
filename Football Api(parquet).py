import requests
import json
import os
import pandas as pd
import awswrangler as wr
import boto3 
from dotenv import load_dotenv
url = 'http://api.football-data.org/v4/competitions/'
response = requests.get(url)
response_dict = response.json()

test1 = response_dict['competitions']
df = pd.json_normalize(test1)

#AWS credentials
aws_access_key_id = os.getenv('ACCESS_KEY')
aws_secret_access_key = os.getenv('SECRET_KEY')
aws_region = os.getenv('region')

#the S3 path where the Parquet file will be saved
path_s3 = 's3://kayceesecondassignment/FootballApi.parquet'


# Upload the DataFrame to S3 as a Parquet file using awswrangler
wr.s3.to_parquet(
    df= df,
    path=path_s3,
    dataset=True,  
    mode='append',
    boto3_session=session 
)


