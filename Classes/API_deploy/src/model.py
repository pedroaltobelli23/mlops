import pickle
import boto3
import os
from dotenv import load_dotenv

def load_model(s3):
    
    obj = s3.get_object(
        Bucket=os.getenv("AWS_BUCKET_NAME"),
        Key="pedroatp/model.pkl",
    )
    
    model_file = obj["Body"].read()
        
    return pickle.loads(model_file)


def load_encoder(s3):
    obj = s3.get_object(
        Bucket=os.getenv("AWS_BUCKET_NAME"),
        Key="pedroatp/ohe.pkl",
    )
    
    ohe_file = obj["Body"].read()
        
    return pickle.loads(ohe_file)