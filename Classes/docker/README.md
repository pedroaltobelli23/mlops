# Class 05 - Docker

## S3 Bucket
- Read file from S3 bucket:
python read_file_from_s3.py

- Upload file to S3 bucket:
python upload_file_to_s3.py

- Create S3 bucket folder:
python create_folder_s3.py

### .env file format

'''env
AWS_ACCESS_KEY_ID="XXXXXXXXXXXXXXXXXXXXX"
AWS_SECRET_ACCESS_KEY="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
AWS_BUCKET_NAME="some-bucket-name"
'''

## Docker
It is necessary to dowload docker and DBeaver

- Load a docker PostgreSQL database serivce:
docker run -d --name postgres-mlops -p 5100:5432 -e POSTGRES_PASSWORD=abc123 -v pg-data:/var/lib/postgresql/data postgres

- Open DBeaver and create a database connection. Use as credentials:

"""Bash
HOST: "localhost"
USERNAME: "postgres"
PASSWORD: "abc123"
DB: "postgres"
PORT: 5100
"""

- Create schema inside this dataset:

"""sql
CREATE SCHEMA IF NOT EXISTS sales;
CREATE SCHEMA IF NOT EXISTS sales_analytics;

DROP TABLE IF EXISTS sales.item_sale;
CREATE TABLE sales.item_sale (
  id SERIAL PRIMARY KEY,
  store_id integer,
  client_id integer,
  product_id integer,
  date_sale DATE,
  price decimal(10,2)
);


DROP INDEX IF EXISTS item_sale_store_id_idx;
CREATE INDEX IF NOT EXISTS item_sale_store_id_idx ON sales.item_sale (store_id,date_sale);

INSERT INTO sales.item_sale
    (store_id, client_id, product_id, date_sale, price)
VALUES
    (5000, 148331, 1715, '2022-01-01', 362.16),
    (5000, 203423, 1921, '2022-01-01', 334.23),
    (5000, 192737, 1667, '2022-01-01', 351.77),
    (5005, 369515, 2131, '2023-08-22', 877.95);
"""