from config_path import ENV_PATH, DATA_PATH
from os import environ
from pathlib import Path
import pandas as pd

# Specify the path of kaggle json token
environ['KAGGLE_CONFIG_DIR'] = str(ENV_PATH)

# Authenticate
import kaggle
kaggle.api.authenticate()

# Download kaggle dataset and metadata
# kaggle.api.dataset_download_files('syedanwarafridi/vehicle-sales-data', path=DATA_PATH, unzip=True)

# Get the datasets
csv_files = list(DATA_PATH.glob('*.csv'))
csv_file = csv_files[0]

#
df = pd.read_csv(csv_file)

# Define the main function
def main() -> bool:
    
    
    return True

# Run the main function
if __name__ == "__main__":
    if main():
        print("Ingestion Complete!")
    else:
        print(f"{Path(__file__).name} Failed!")