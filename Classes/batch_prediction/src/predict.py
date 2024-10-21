import pandas as pd
import argparse
import pickle

# Initialize the argument parser
parser = argparse.ArgumentParser(description="A script that processes an argument.")

parser.add_argument('model', type=str, help="model path")

parser.add_argument('predict_data', type=str, help="predict data path")

# Parse the arguments
args = parser.parse_args()


df = pd.read_parquet(args.predict_data)

with open(args.model, "rb") as f:
    model = pickle.load(f)
    
prediction = model.predict(df)

df["prediction"] = prediction

predict_done = args.predict_data.split(".parquet")[0] + "-done.parquet"

df.to_parquet(predict_done)