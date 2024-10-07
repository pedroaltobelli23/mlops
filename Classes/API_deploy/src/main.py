from fastapi import FastAPI
import pandas as pd
from model import load_model, load_encoder
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, Depends, Body
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
import boto3
import os
from dotenv import load_dotenv

class Person(BaseModel):
    age: int
    job: str
    marital: str
    education: str
    balance: int
    housing: str
    duration: int
    campaign: int

app = FastAPI()

bearer = HTTPBearer()

@app.get("/")
async def root():
    """
    Route to check that API is alive!
    """
    return "Model API is alive!"

from fastapi import FastAPI, Body

from typing import Annotated

def get_username_for_token(token):
    if token == "abc123":
        return "pedro1"
    return ""

async def validate_token(credentials: HTTPAuthorizationCredentials = Depends(bearer)):
    token = credentials.credentials

    username = get_username_for_token(token)
    if username == "":
        raise HTTPException(status_code=401, detail="Invalid token")

    return {"username": username}

ml_models = {}

@app.on_event("startup")
async def startup_event():
    s3 = boto3.client(
        "s3",
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    )
    
    ml_models["ohe"] = load_encoder(s3)
    ml_models["model"] = load_model(s3)
    
    

@app.post("/predict")
async def predict(
    person: Annotated[
        Person,
        Body(examples=[{"age": 42,"job": "entrepreneur","marital": "married","education": "primary","balance": 558,"housing": "yes","duration": 186,"campaign": 2}]),
    ],
    user=Depends(validate_token),
):
    ohe = ml_models["ohe"]
    model = ml_models["model"]

    person_t = ohe.transform(pd.DataFrame([person.dict()]))
    pred = model.predict(person_t)[0]

    return {
        "prediction": str(pred),
        "username": user["username"]
        }