import pandas as pd
from pymongo import MongoClient
import requests
from io import BytesIO
import numpy as np

def parse_double_key_signle_val(df: pd.DataFrame):
    header_cell = str(df.columns[0])
    
    keys, val_name = [part.strip() for part in header_cell.split("->", 1)]
    key1_name, key2_name = [part.strip() for part in keys.split("\\", 1)]

    key1_values = df.iloc[:, 0]
    key2_values = df.columns[1:]
    data = []

    for i, key1 in enumerate(key1_values):
        for key2 in key2_values:
            val = df.iloc[i, df.columns.get_loc(key2)]
            if pd.notnull(val):
                data.append({key1_name: key1, key2_name: key2, val_name: val})
    
    return data



def parse_double_key_multiple_val(df: pd.DataFrame):
    return

def parse_sheet_with_2_keys(df: pd.DataFrame):
    header_cell = str(df.columns[0])
    
    contains_single_value: bool = False
    if "->" in header_cell:
        contains_single_value = True

    if contains_single_value:
        return parse_double_key_signle_val(df)
    else:
        return parse_double_key_multiple_val(df)

def parse_sheet_with_single_key(df: pd.DataFrame) -> list[dict]:
    return df.to_dict(orient='records')


def load_db_from_google_sheets(sheet_names:list[str], mongo_uri:str, db_name:str, drop_old_collections: bool = True):
    # Connect to MongoDB
    client = MongoClient(mongo_uri)
    db = client[db_name]
    
    # Excel export URL (downloads the whole spreadsheet as .xlsx)
    sheet_id = "1EZzJBHdRWpiYhxwvx7hM9AJnGprLlPj6sEou0YIm7R0"
    export_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=xlsx"

    # Request and load as Excel file
    response = requests.get(export_url)
    xls = pd.ExcelFile(BytesIO(response.content))

    for sheet_name in sheet_names:
        sheet_df = xls.parse(sheet_name)
        sheet_df = sheet_df.astype(object)

        is_table_with_2_keys: bool = False
        if "\\" in str(sheet_df.columns[0]):
            is_table_with_2_keys = True
        
        data = None
        if (is_table_with_2_keys):
            data = parse_sheet_with_2_keys(sheet_df)
        else:
            data = parse_sheet_with_single_key(sheet_df)

        # Insert into MongoDB
        collection = db[sheet_name]
        if (drop_old_collections):
            collection.drop()
            print(f"Previous data in '{sheet_name}' collection droped.")

        
        if data:  # Make sure there's data to insert
            collection.insert_many(data)
            print(f"Inserted {len(data)} documents into '{sheet_name}' collection.")
        else:
            print(f"No data to insert in '{sheet_name}'.")


    return


mongo_uri = "mongodb+srv://admin:admin@energycalculator.e5mcb.mongodb.net/?retryWrites=true&w=majority&appName=EnergyCalculator"
db_name = "EnergyCalculator"
all_sheet_names = [
    'airtightness_types',
    'air_circulation_factors',
    'construction_periods',
    'districts',
    'door_u_values',
    'dwelling_types',
    'efficiency_coefs',
    'glazing_types',
    'heating_fuels',
    'heating_systems',
    'insulated_surfaces',
    'joinery_materials',
    'months',
    'municipalities',
    'surface_u_values',
    'unit_needed_energy',   
    'window_u_values',
    'wind_exposure_types'
]

load_db_from_google_sheets(all_sheet_names, mongo_uri, db_name, drop_old_collections=True)
