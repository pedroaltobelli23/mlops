# mlops-aps01-marketing

![svg](https://mlops.macielvidal.com/webhook/svg/24_2/pedroaltobelli23)

MLOps &amp; Interviews - APS01

Run the files in order to make the preprocessing, training and prediction.

process.py
train.py
predict.py

- process.py: Create "bank_predict.csv" that will be used for prediction and "preprocess_bank.csv" that will be used for training.

- train.py: Train the model with LightGBM simple.

- predict.py: Predict using the model and the OHE created in train.py and put it into a column called y_pred in the "bank_predict.csv" file.