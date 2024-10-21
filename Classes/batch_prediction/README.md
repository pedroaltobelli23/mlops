# Class 03 - Batch Prediction

1. Generate train data
Inside src folder:
- python get_data.py 2022 01 01 2023 08 01 train

This will create a train-2023-08-01.csv file in the data folder containing the sales data for each company's store.

2. Preprocess the data into a parquet file and add the weekday feature
Inside src folder:
- python process.py ../data/train-2023-08-01.csv 

This will create a parquet file with the csv file as input

3. Train the model using the parquet data
Inside src folder:
- python train.py ../data/train-2023-08-01.parquet

This will create a pickle file with the model

4. Simulate prediction data and make predictions
Inside src folder:
- python get_data.py 2023 08 02 2023 08 03 predict

This will create a parquet file with data to be predicted

5. Making predictions
Inside src folder:
- python predict.py ../models/model.pkl ../data/predict-2023-08-03.parquet