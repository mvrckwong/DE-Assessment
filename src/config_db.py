from os import getenv
from sqlalchemy import create_engine
from dotenv import load_dotenv
from config_path import PROJECT_PATH, ENV_PATH


def db_connection():
    """ Establish a connection to a PostgreSQL database using the provided connection URL. """
    # Standard configuration 
    env_file = ENV_PATH / '.env'
    if not env_file.exists():
        raise FileNotFoundError(f"Environment file {env_file} not found!")
    else:
        load_dotenv(env_file)
    
    db_creds_var = ['DB_USER', 'DB_PW', 'DB_HOST', 'DB_NAME']
    for var in db_creds_var:
        if getenv(var)=='':
            raise ValueError(f'Environment variable {var} not set')
    
    # Database Connection URL and Create the SQLAlchemy engine
    connect_url = f"postgresql://{getenv('DB_USER')}:{getenv('DB_PW')}@{getenv('DB_HOST')}/{getenv('DB_NAME')}?sslmode=prefer"
    engine = create_engine(connect_url)
    return engine
 

# Running the main function
if __name__ == "__main__":
    print(db_connection())
    None