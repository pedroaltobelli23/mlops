import json
import pickle
import lightgbm
import pandas as pd
import os
import boto3

def startup_event():
    s3 = boto3.client(
        "s3",
        aws_access_key_id=os.getenv("ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("SECRET_ACCESS_KEY"),
        region_name=os.getenv("REGION"),
    )
    
    obj = s3.get_object(
        Bucket=os.getenv("BUCKET_NAME"),
        Key="pedroatp/model.pkl",
    )
    
    model_file = obj["Body"].read()
    loaded_model = pickle.loads(model_file)
    
    obj = s3.get_object(
        Bucket=os.getenv("BUCKET_NAME"),
        Key="pedroatp/ohe.pkl",
    )
    
    ohe_file = obj["Body"].read()
    loaded_ohe = pickle.loads(ohe_file)
    return loaded_model,loaded_ohe

def predict(event, context):
    if "body" not in event:
        return {"error": f"No body provided"}
    
    raw_json = event["body"]
    
    body = json.loads(raw_json)
    
    features_names = ["age","job","marital","education","balance","housing","duration","campaign"]
    
    if len(body)==len(features_names):
        for name in features_names:
            if name not in body:
                return {"error": f"No {name} provided"}
    else:
        return {"error":f"body has {len(body)} features, while model accepts only {len(features_names)} features"}
    
    model,ohe = startup_event()
    body = {"age": 42,"job": "entrepreneur","marital": "married","education": "primary","balance": 558,"housing": "yes","duration": 186,"campaign": 2}
    encoded_features = ohe.transform(pd.DataFrame([body]))
    predicttion = model.predict(encoded_features)[0]
    
    res = {"result":str(predicttion)}
    
    return res
