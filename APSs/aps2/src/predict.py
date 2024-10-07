import pandas as pd
import argparse
import pickle
from sqlalchemy import create_engine,text
from dotenv import load_dotenv
import os

load_dotenv()

dbname = os.getenv("DB_DATABASE")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
user = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")

# Connecting with database
db_connection_str = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}'

engine = create_engine(db_connection_str)

# Getting the data to be predicted
with open("../data/retrievepredict.sql",'r') as f:
    query = f.read()
    df_to_predict = pd.read_sql_query(query, engine)

parser = argparse.ArgumentParser(description="A script that processes an argument.")

parser.add_argument('model', type=str, help="model path")

args = parser.parse_args()

with open(args.model, "rb") as f:
    model = pickle.load(f)

# model predict function
predictions = model.predict(df_to_predict.drop(columns=["total_sales"]))

df_to_predict["total_sales"] = predictions

with engine.connect() as con:
    
    for i in range(len(df_to_predict)):
        row = df_to_predict.iloc[i,:]
        columns = row.to_dict()
        command = text("""UPDATE sales_analytics.scoring_ml_pedroatp SET total_sales = :total_sales WHERE store_id = :store_id AND year = :year AND month = :month AND day = :day AND weekday = :weekday""")
        con.execute(command,columns)
        con.commit()

# Validate
with open("../data/retrievepredict.sql",'r') as f:
    query = f.read()
    df_predicted = pd.read_sql_query(query, engine)

print(df_predicted)