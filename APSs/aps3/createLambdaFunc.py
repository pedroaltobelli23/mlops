import boto3
import os
from dotenv import load_dotenv

load_dotenv()

# Provide function name: "ex_docker_<INSPER_USERNAME>"
function_name = os.getenv("LAMBDA_FUNCT_NAME")

image_uri = os.getenv("IMAGE_URI")+":latest"

lambda_role_arn = os.getenv("AWS_LAMBDA_ROLE_ARN")

# Create a Boto3 client for AWS Lambda
lambda_client = boto3.client(
    "lambda",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION"),
)

# Delete AWS Lambda that already exists
try:
    response = lambda_client.delete_function(FunctionName=function_name)
except Exception as e:
    print(f"Error deleting function: {str(e)}")

response = lambda_client.create_function(
    FunctionName=function_name,
    PackageType="Image",
    Code={"ImageUri": image_uri},
    Role=lambda_role_arn,
    Timeout=30,  # Optional: function timeout in seconds
    MemorySize=128,  # Optional: function memory size in megabytes
    Environment = {
        "Variables": {
            "BUCKET_NAME": os.getenv("AWS_BUCKET_NAME"),
            "ACCESS_KEY_ID":os.getenv("AWS_ACCESS_KEY_ID"),
            "SECRET_ACCESS_KEY":os.getenv("AWS_SECRET_ACCESS_KEY"),
            "REGION":os.getenv("AWS_REGION"),
        }
    }
)

print("Lambda function created successfully:")
print(f"Function Name: {response['FunctionName']}")
print(f"Function ARN: {response['FunctionArn']}")