# mlops-API-class-02
APi from class 02 

How to run:

Create env file:
```bash
AWS_ACCESS_KEY_ID="ACCESS KEY ID"
AWS_SECRET_ACCESS_KEY="SECRET ACCESS KEY"
AWS_BUCKET_NAME="BUCKET NAME"
```

Start API:
```bash
uvicorn main:app --host 0.0.0.0 --port 8900 --reload
```

Use the script testAPI.py to test it:
```bash
python3 testAPI.py
```

Use the file put_models_pkl_inS3.py to save the model and encoder inside a S3 Bucket