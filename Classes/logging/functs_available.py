import boto3
import os
from dotenv import load_dotenv

load_dotenv()

# Create a Boto3 client for AWS Lambda
lambda_client = boto3.client(
    "lambda",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION"),
)

# List to store all Lambda functions
all_functions = []

# Initial request
response = lambda_client.list_functions(MaxItems=1000)

# Add the functions to the list
all_functions.extend(response['Functions'])

# Keep retrieving while there's a NextMarker
while 'NextMarker' in response:
    response = lambda_client.list_functions(Marker=response['NextMarker'], MaxItems=1000)
    all_functions.extend(response['Functions'])

# Print total number of Lambda functions
print(f"You have {len(all_functions)} Lambda functions")

# Print the name of each Lambda function
if len(all_functions) > 0:
    print("Here are their names:")
    for function in all_functions:
        function_name = function['FunctionName']
        print(function_name)
