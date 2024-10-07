import boto3
import os
from dotenv import load_dotenv

load_dotenv()

print("Starting uploading")

s3 = boto3.client(
    "s3",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
)

s3.upload_file(
    "models/model.pkl",  # Local Filepath
    os.getenv("AWS_BUCKET_NAME"),  # Bucket name
    "pedroatp/model.pkl",  # Key (path on bucket)
)

print("First upload ended")

s3.upload_file(
    "models/ohe.pkl",  # Local Filepath
    os.getenv("AWS_BUCKET_NAME"),  # Bucket name
    "pedroatp/ohe.pkl",  # Key (path on bucket)
)