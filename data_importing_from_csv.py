import numpy as np
import pandas as pd

# RUN THIS FILE WHEN MUNICIPALITIES AND DISTRICTS ARE CHANGED
# TO REGENERATE PYTHON STRUCTURES IN municipalities.py AND districts.py


# Reads the data from csv and automaticly creates enum for municipalities
# and puts all important parameters in arrays
def create_municipalities_py_from_csv_data(input_csv):
    output_file_name = "municipalities.py"
    
    # Reading csv and importing is as pandas datafreame
    opstine_df = pd.read_csv(input_csv, encoding="utf-8")

    opstine_df['Naziv latinica'] = opstine_df['Naziv latinica'].astype(str)

    latin_names_array = opstine_df['Naziv latinica'].to_numpy()

    with open(output_file_name, "w", encoding="utf-8") as f:
        f.write("from enum import Enum\n\n")
        f.write("from districts import *\n\n")

        f.write("class SrbMunicipalities(Enum):\n")

        id = 0
        for name in latin_names_array:
            f.write(f'\t{name.upper().replace(" ", "_")} = {id}\n')
            id = id + 1

    opstine_df['Naziv opstine'] = opstine_df['Naziv opstine'].astype(str)

    cyrilic_names_array = opstine_df['Naziv opstine'].to_numpy()
    
    with open(output_file_name, "r+", encoding="utf-8") as f:
        f.seek(0, 2) # Move to the end of the file
        f.write("\nmunicipality_names = [\n")
        
        for name in cyrilic_names_array:
            f.write(f'\t"{name}",\n')
            
        f.seek(f.tell() - 3)
        f.write("\n]")
    
    HDD_vals = opstine_df['HDD'].to_numpy()
    
    with open(output_file_name, "r+", encoding="utf-8") as f:
        f.seek(0, 2) # Move to the end of the file
        f.write("\nmunicipality_HDDs = [\n")
        
        for HDD_val in HDD_vals:
            f.write(f'\t{HDD_val},\n')
            
        f.seek(f.tell() - 3)
        f.write("\n]")
    
    opstine_df['okrug latinica'] = opstine_df['okrug latinica'].astype(str)

    districts = opstine_df['okrug latinica'].to_numpy()

    with open(output_file_name, "r+", encoding="utf-8") as f:
        f.seek(0, 2) # Move to the end of the file
        f.write("\ncorresponding_districts = [\n")
        
        for district in districts:
            f.write(f'\tSrbDistricts.{district.upper().replace(" ", "_")},\n')
                    
        f.seek(f.tell() - 3)
        f.write("\n]")

# Reads the data from csv and automaticly creates enum for districts
# and puts all important parameters in arrays
def create_districts_py_from_csv_data(input_csv):
    output_file_name = "districts.py"
    distrct_df = pd.read_csv(input_csv, encoding="utf-8")

    distrct_df['region latinica'] = distrct_df['region latinica'].astype(str)

    latin_names_array = distrct_df['region latinica'].to_numpy()

    with open(output_file_name, "w", encoding="utf-8") as f:
        f.write("from enum import Enum\n\n")
        f.write("class SrbDistricts(Enum):\n")

        id = 0
        for name in latin_names_array:
            f.write(f'\t{name.upper().replace(" ", "_")} = {id}\n')
            id = id + 1

    distrct_df['region naziv'] = distrct_df['region naziv'].astype(str)

    cyrilic_names_array = distrct_df['region naziv'].to_numpy()
    
    with open(output_file_name, "r+", encoding="utf-8") as f:
        f.seek(0, 2) # Move to the end of the file
        f.write("\ndistrict_names = [\n")
        
        for name in cyrilic_names_array:
            f.write(f'\t"{name}",\n')
            
        f.seek(f.tell() - 3)
        f.write("\n]")
    
    solar_prod_roof = distrct_df['proizvodnja krov(MWh/MWp)'].to_numpy()
    
    with open(output_file_name, "r+", encoding="utf-8") as f:
        f.seek(0, 2) # Move to the end of the file
        f.write("\n\nroof_solar_production = [\n")
        
        for prod_val in solar_prod_roof:
            f.write(f'\t{prod_val},\n')
            
        f.seek(f.tell() - 3)
        f.write("\n]")
    
    solar_prod_land = distrct_df['proizvodnja tlo(MWh/MWp)'].to_numpy()
    
    with open(output_file_name, "r+", encoding="utf-8") as f:
        f.seek(0, 2) # Move to the end of the file
        f.write("\n\nland_solar_production = [\n")
        
        for prod_val in solar_prod_land:
            f.write(f'\t{prod_val},\n')
            
        f.seek(f.tell() - 3)
        f.write("\n]")

create_municipalities_py_from_csv_data("Opstine.csv")
create_districts_py_from_csv_data("okruzi.csv")
