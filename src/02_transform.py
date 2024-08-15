from config_path import ENV_PATH, DATA_PATH, OUTPUT_PATH
from config_db import db_connection
from pathlib import Path
import pandas as pd
import numpy as np


def create_dim_tbl(data:pd.DataFrame) -> tuple:
    ''' Create the dimension table based on the existing data. '''
    
    # Create dimension tables with an ID column for each
    dim_year = data['year'].dropna().drop_duplicates().sort_values().to_frame().reset_index(drop=True)
    
    # Develop the dimension table, add the id, and sort the columns
    dim_transmission = data['transmission'].dropna().drop_duplicates().sort_values().to_frame().reset_index(drop=True)
    dim_transmission['transmission_id'] = dim_transmission.index + 1
    dim_transmission = dim_transmission[['transmission_id', 'transmission']]
    
    # Develop the dimension table, add the id, and sort the columns
    dim_seller = data['seller'].dropna().drop_duplicates().sort_values().to_frame().reset_index(drop=True)
    dim_seller['seller_id'] = dim_seller.index + 1
    dim_seller = dim_seller[['seller_id', 'seller']]
    
    # Develop the dimension table, add the id, and sort the columns
    dim_state = data['state'].dropna().drop_duplicates().sort_values().to_frame().reset_index(drop=True)
    dim_state['state_id'] = dim_state.index + 1
    dim_state = dim_state[['state_id', 'state']]
    
    # Develop the dimension table, add the id, and sort the columns
    dim_maker = data['make'].dropna().drop_duplicates().sort_values().to_frame().reset_index(drop=True)
    dim_maker['make_id'] = dim_maker.index + 1
    dim_maker = dim_maker[['make_id', 'make']]
    
    return dim_year, dim_transmission, dim_seller, dim_state, dim_maker

def transform_fact_tbl(data:pd.DataFrame) -> pd.DataFrame:
    
    # Filter the bad data, then transform fact table
    data = data[data['make'] != 'Volkswagen']   # Bad data from Volkswagen, remove (TEMP SOLUTION)
    
    # Capitalize and strip, then replace
    columns_to_cap = ['transmission', 'seller', 'color', 'make', 'interior']
    data[columns_to_cap] = data[columns_to_cap].apply(lambda x: x.str.title().str.strip())
    data['state'] = data['state'].str.upper().str.strip()
    data['color'] = data['color'].replace('‚Äî', np.nan)
    
    # Rename Columns
    data.rename(
        columns={
            'color': 'exterior_color',
            'interior': 'interior_color',
        }, 
        inplace=True
    )
    
    return data

##########################
# Define the main function
##########################

def main() -> bool:
    CURRENT_SCHEMA = 'stg'
    ENGINE = db_connection()
    
    # Read data from the raw schema
    raw_df = pd.read_sql_table('raw_car_prices', ENGINE, schema='raw')
    
    # Transform main data
    fact_data = transform_fact_tbl(data=raw_df)
    
    # Create dimension tables
    dim_year, dim_transmission, dim_seller, dim_state, dim_maker = \
        create_dim_tbl(data=raw_df)
        
    # Create the fact table
    fact_car_prices = raw_df.copy()
    
    fact_car_prices = fact_car_prices.merge(dim_maker[['make', 'make_id']], on='make', how='left')
    fact_car_prices.to_csv(OUTPUT_PATH / 'fact.csv', index=False)
        
    # Map the foreign keys from dimension tables to the fact table
    # fact_data = fact_data.merge(dim_transmission[['transmission', 'transmission_id']], on='transmission', how='left')
    
    # dim_transmission.to_csv(OUTPUT_PATH / 'dim_transmission.csv', index=False)
    # fact_data.to_csv(OUTPUT_PATH / 'fact_table.csv', index=False)
    
    # Select relevant columns
    year,make,model,trim,body,transmission,vin,state,condition,odometer,exterior_color,interior_color,seller,mmr,sellingprice,saledate,
    
    return True


# Run the main function
if __name__ == "__main__":
    if main():
        print(f"{Path(__file__).name} Complete!")
    else:
        print(f"{Path(__file__).name} Failed!")
