from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

dbname = os.getenv("DB_DATABASE")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
user = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")

db_connection_str = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}'

engine = create_engine(db_connection_str)

with open("../data/train.sql",'r') as f:
    query = f.read()
    df = pd.read_sql_query(query, engine)

print(df)

df.to_parquet("../data/train_data.parquet")

print("df saved into file ../data/train_data.parquet")