import pandas as pd
from sqlalchemy import create_engine

# SQL connection details
database_config = {
    'dbname': 'car_db',
    'user': 'username',
    'password': 'password',
    'host': 'localhost',
    'port': '5432'
}

# Create SQLAlchemy engine
engine = create_engine(f"postgresql://{database_config['user']}:{database_config['password']}@{database_config['host']}:{database_config['port']}/{database_config['dbname']}")

# Read data from the raw schema
raw_df = pd.read_sql_table('car_prices', engine, schema='raw')

# Create dimension tables for make, model, trim, seller, and date
make_dim = raw_df[['make']].drop_duplicates().reset_index(drop=True)
model_dim = raw_df[['model']].drop_duplicates().reset_index(drop=True)
trim_dim = raw_df[['trim']].drop_duplicates().reset_index(drop=True)
seller_dim = raw_df[['seller']].drop_duplicates().reset_index(drop=True)
date_dim = pd.to_datetime(raw_df['saledate']).dt.date.drop_duplicates().reset_index(drop=True)

# Add surrogate keys to dimension tables
make_dim['make_id'] = make_dim.index + 1
model_dim['model_id'] = model_dim.index + 1
trim_dim['trim_id'] = trim_dim.index + 1
seller_dim['seller_id'] = seller_dim.index + 1
date_dim = pd.DataFrame({'date': date_dim, 'date_id': date_dim.index + 1})

# Create the fact table by merging with dimension tables
fact_car_sales = raw_df.copy()
fact_car_sales['saledate'] = pd.to_datetime(fact_car_sales['saledate']).dt.date
fact_car_sales = pd.merge(fact_car_sales, make_dim, on='make')
fact_car_sales = pd.merge(fact_car_sales, model_dim, on='model')
fact_car_sales = pd.merge(fact_car_sales, trim_dim, on='trim')
fact_car_sales = pd.merge(fact_car_sales, seller_dim, on='seller')
fact_car_sales = pd.merge(fact_car_sales, date_dim, left_on='saledate', right_on='date')

# Select relevant columns for the fact table
fact_car_sales = fact_car_sales[['make_id', 'model_id', 'trim_id', 'seller_id', 'date_id', 'year', 'sellingprice', 'odometer', 'transmission']]

# Write dimension tables to the staging schema
make_dim.to_sql('dim_make', engine, schema='staging', if_exists='replace', index=False)
model_dim.to_sql('dim_model', engine, schema='staging', if_exists='replace', index=False)
trim_dim.to_sql('dim_trim', engine, schema='staging', if_exists='replace', index=False)
seller_dim.to_sql('dim_seller', engine, schema='staging', if_exists='replace', index=False)
date_dim.to_sql('dim_date', engine, schema='staging', if_exists='replace', index=False)

# Write the fact table to the staging schema
fact_car_sales.to_sql('fact_car_sales', engine, schema='staging', if_exists='replace', index=False)
