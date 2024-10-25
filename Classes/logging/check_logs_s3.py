import os
import boto3
from dotenv import load_dotenv

load_dotenv()

bucket_name = "my-log-bucket-1"
# Same key from previous source code
key = "log1"

s3 = boto3.client(
    "s3",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION"),
)

obj = s3.get_object(Bucket=bucket_name, Key=key)

file_content = obj["Body"].read().decode("utf-8")

print("Stored log:")
print(file_content)