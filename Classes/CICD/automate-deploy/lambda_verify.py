import io
import os
import boto3
import json
from dotenv import load_dotenv

load_dotenv()

function_name = "my_wc_function10"

# Create a Boto3 client for AWS Lambda
lambda_client = boto3.client(
    "lambda",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION"),
)

msg = {"body": "hello from mars"}

try:
    print(f"Message:\n{msg}")

    response = lambda_client.invoke(
        FunctionName=function_name,
        InvocationType="RequestResponse",
        Payload=json.dumps(msg),
    )

    payload = response["Payload"]

    txt = io.BytesIO(payload.read()).read().decode("utf-8")
    print(f"\nResponse:\n{txt}")
except Exception as e:
    print(e)