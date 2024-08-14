from pathlib import Path

# Define the base path for your project
SRC_PATH:Path = Path(__file__).parent
PROJECT_PATH:Path = SRC_PATH.parent

# Define the paths for your project
LOGS_PATH:Path = PROJECT_PATH / 'logs'
OUTPUT_PATH:Path = PROJECT_PATH / '.output'
ENV_PATH:Path = PROJECT_PATH / 'environment'
DATA_PATH: Path = PROJECT_PATH / 'data'

if __name__ == "__main__":
    None