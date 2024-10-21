import pandas as pd
import numpy as np
import pickle
import argparse
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Initialize the argument parser
parser = argparse.ArgumentParser(description="A script that processes an argument.")

# Define the arguments the script expects
parser.add_argument('file', type=str, help="file path")

# Parse the arguments
args = parser.parse_args()


df = pd.read_parquet(args.file)

X = df.drop("total_sales", axis=1)
y = df["total_sales"]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=1912)

model = RandomForestRegressor(n_estimators=100, random_state=195)
print("Training model...")
model.fit(X_train, y_train)
print("Sucessfully trained")

# Evaluation
y_pred = model.predict(X_test)

# Mean Absolute Error (MAE)
mae = mean_absolute_error(y_test, y_pred)
print(f'Mean Absolute Error (MAE): {mae}')

# Mean Squared Error (MSE)
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error (MSE): {mse}')

# Root Mean Squared Error (RMSE)
rmse = np.sqrt(mse)
print(f'Root Mean Squared Error (RMSE): {rmse}')

# R-squared (R²)
r2 = r2_score(y_test, y_pred)
print(f'R-squared (R²): {r2}')

print("saving model")

# Specify the file path where you want to save the pickle file
file_path = "../models/model.pkl"

# Save the model as a pickle file
with open(file_path, "wb") as f:
    pickle.dump(model, f)
    
print("model sucessfully saved")