# 24-2-mlops-aps02-pedroaltobelli23

APS: New version of the APS1 using batch prediction and sql

1. Get the data inside the database and save into parquet file 
```Bash
cd src/

python3 get_data.py
```

2. Train model using data
```Bash
python3 train.py ../data/train_data.parquet
```

3. Use predict.sql inside DBeaver to create table that will be predicted 

4. Predict using the trained model
```Bash
python3 predict.py ../models/model.pkl
```
