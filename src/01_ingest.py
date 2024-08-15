from config_path import ENV_PATH, DATA_PATH
from config_db import db_connection

from os import environ
from pathlib import Path
import pandas as pd

# Define the main function
def main() -> bool:
    CURRENT_SCHEMA = 'raw'
    ENGINE = db_connection()
    
    # Specify the path of kaggle json token P
    environ['KAGGLE_CONFIG_DIR'] = str(ENV_PATH)

    # Authenticate
    import kaggle
    kaggle.api.authenticate()

    # Get the datasets
    csv_files = list(DATA_PATH.glob('*.csv'))

    # Loop through the located csv files
    for file in csv_files:
        df = pd.read_csv(file)
        df.to_sql(
            name=f'raw_{file.stem}', 
            con=ENGINE, 
            if_exists='replace', 
            index=False,
            schema=CURRENT_SCHEMA
        )
    
    return True

# Run the main function
if __name__ == "__main__":
    if main():
        print(f"{Path(__file__).name} Complete!")
    else:
        print(f"{Path(__file__).name} Failed!")