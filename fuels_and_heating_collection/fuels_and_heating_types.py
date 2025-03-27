import pandas as pd
from dataclasses import dataclass

@dataclass
class CoefficientsModel:
    fuel_efficency: float
    pipe_system_efficency: float
    regulation_efficency: float

fuels_df: pd.DataFrame = pd.read_csv("fuels_and_heating_collection/goriva.csv")
coefficients_df: pd.DataFrame = pd.read_csv("fuels_and_heating_collection/koeficijenti.csv")
heating_types_df: pd.DataFrame = pd.read_csv("fuels_and_heating_collection/tipovi_grejanja.csv")

coefficients_df.set_index(["fuel_type_cyrillic", "heating_type_cyrillic"], inplace=True)

# BACKEND -> DB (csv file) API

def __db_get_all_fuel_types_lat() -> list[str]:
	fuel_types_lat: list[str] = fuels_df['fuel_type_latin'].tolist()
	
	return fuel_types_lat

def __db_get_all_fuel_types_cyr() -> list[str]:
	fuel_types_cyr: list[str] = fuels_df['fuel_type_cyrillic'].tolist()

	return fuel_types_cyr

def __db_get_all_heating_types_lat() -> list[str]:
	fuel_types_lat: list[str] = heating_types_df['heating_type_latin'].tolist()
	
	return fuel_types_lat

def __db_get_all_heating_types_cyr() -> list[str]:
	fuel_types_cyr: list[str] = heating_types_df['heating_type_cyrillic'].tolist()

	return fuel_types_cyr

def __db_get_coefficents(fuel_type_cyr: str, heating_type_cyr: str) -> CoefficientsModel:
    coeffs = coefficients_df.loc[(fuel_type_cyr, heating_type_cyr)]
        
    # Convert to dataclass
    return CoefficientsModel(
        fuel_efficency=float(coeffs["fuel_efficency"]),
        pipe_system_efficency=float(coeffs["pipe_system_efficency"]),
        regulation_efficency=float(coeffs["pipe_system_efficency"])
    )

# FRONTEND -> BECKEND API

def be_get_all_fuel_types_lat() -> list[str]:	
    return __db_get_all_fuel_types_lat()


def be_get_all_fuel_types_cyr() -> list[str]:	
    return __db_get_all_fuel_types_cyr()


def be_get_all_heating_types_lat() -> list[str]:	
    return __db_get_all_heating_types_lat()


def be_get_all_heating_types_cyr() -> list[str]:	
    return __db_get_all_heating_types_cyr()

def be_get_coefficents(fuel_type_cyr: str, heating_type_cyr: str) -> CoefficientsModel:
    return __db_get_coefficents(fuel_type_cyr, heating_type_cyr)
