# Data
import pandas as pd
import os
import argparse

# Export
import pickle

# Plot
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno

# Initialize the argument parser
parser = argparse.ArgumentParser(description="A script that processes an argument.")

# Define the arguments the script expects
parser.add_argument('file', type=str, help="file path")

# Parse the arguments
args = parser.parse_args()

input_file = args.file

df = pd.read_csv(input_file)

df['date'] = pd.to_datetime(df['date'])

# df = df.drop(columns=["date"])

# Group by 'Date' and 'store_id', then sum the 'price' column
new_df = df.groupby(['date', 'store_id'])['price'].sum().reset_index()

# Rename the 'price' column to 'total_sales'
new_df = new_df.rename(columns={'price': 'total_sales'})

# Extract year, month, day, and weekday
new_df['year'] = new_df['date'].dt.year
new_df['month'] = new_df['date'].dt.month
new_df['day'] = new_df['date'].dt.day
new_df['weekday'] = new_df['date'].dt.weekday

new_df = new_df.drop(columns=["date"])
output_file = input_file.replace(".csv",".parquet")
new_df.to_parquet(output_file)
