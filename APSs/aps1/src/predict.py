import pandas as pd
import pickle

# Modeling
from lightgbm import LGBMClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OneHotEncoder

df = pd.read_csv("data/bank_predict.csv")

# Load Model
with open('models/model.pkl', 'rb') as f:
    model = pickle.load(f)
    
# Load OHE
with open('models/ohe.pkl', 'rb') as f:
    ohe = pickle.load(f)
    
df_encoded = ohe.fit_transform(df)

prediction = model.predict(df_encoded)

dep_mapping = {1: "yes", 0: "no"}

# Convert the column to category and map the values
df["y_pred"] = prediction

df["y_pred"] = df["y_pred"].astype("int").map(dep_mapping)

print(df.head())

df.to_csv("data/bank_predict.csv")