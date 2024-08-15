from airflow import DAG
from airflow.decorators import task
from airflow.hooks.postgres_hook import PostgresHook
import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime

# Define the default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 8, 16),
    'retries': 1,
}

# Instantiate the DAG
dag = DAG('csv_to_postgres', default_args=default_args, schedule_interval='@once')

@task
def upload_csv_to_postgres():
    # Read the CSV file into a DataFrame
    df = pd.read_csv('path/to/your/file.csv')

    # Create a SQLAlchemy engine
    postgres_hook = PostgresHook(postgres_conn_id='your_postgres_conn_id')
    engine = create_engine(postgres_hook.get_uri())

    # Upload DataFrame to PostgreSQL
    df.to_sql('your_table_name', engine, if_exists='replace', index=False)

# Define the task in the DAG
upload_task = upload_csv_to_postgres()

# Set task dependencies if needed