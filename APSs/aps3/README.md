# APS3
Pedro Altobelli

How to run:

1. Install dependencies (python 3.10.15):
```bash
pip3 install -r requirements.txt
```

URI = 820926566402.dkr.ecr.us-east-2.amazonaws.com/aps-03-mlops-pedroatp:latest

2. Configure env file:
```bash
AWS_ACCESS_KEY_ID="ACCESS KEY"
AWS_SECRET_ACCESS_KEY="SECRET ACCESS KEY"
AWS_REGION="REGION"
AWS_ACCOUNT_ID="ACCOUNT ID"
AWS_LAMBDA_ROLE_ARN="LAMBDA ROLE ARN"
AWS_BUCKET_NAME="BUCKET NAME"
ECR_REPO_NAME="ECR REPO NAME"
```

3. Create ECR Container Repository (if necessary):
```bash
python3 createContainerRepo.py
```

4. Create S3 Bucket with model and ohe files (if necessary):
```bash
python3 createBucket.py

python3 models_to_s3.py
```

This command will return the repository URI which is necessary for the next steps
4. Export the Uri:
```
export URI="ECR repository URI"
```

5. Build docker image and tag
```bash
chmod +x build_push_docker.sh

./build_push_docker.sh
```

6. Create lambda function. It is necessary to add a filed called IMAGE_URI in the .env file with the ECR repo URI + ":latest"
```bash
python3 createLambdaFunc.py
```

7. Create API
```bash
python3 createAPI.py
```

8. Put the url in the file testAPI.py and run it:
```bash
python3 testAPI.py
```

