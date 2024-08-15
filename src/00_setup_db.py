from config_path import ENV_PATH, DATA_PATH
from config_db import db_connection
from pathlib import Path

# Create an engine instance
engine = db_connection()

# Create schemas
def create_schema(schema_name):
    with engine.connect() as connection:
        connection.execute(f'CREATE SCHEMA IF NOT EXISTS {schema_name};')

def main() -> bool:
    
    try:
        create_schema('raw')
        create_schema('staging') 
        create_schema('production')
    except Exception as e:
        print(e)
        return False
        
    return True

# Run the main function
if __name__ == "__main__":
    if main():
        print(f"{Path(__file__).name} Complete!")
    else:
        print(f"{Path(__file__).name} Failed!")