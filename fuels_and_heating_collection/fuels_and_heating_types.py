import pandas as pd


fuels_df: pd.DataFrame = pd.read_csv("fuels_and_heating_collection/goriva.csv")
coefficients_df: pd.DataFrame = pd.read_csv("fuels_and_heating_collection/koeficijenti.csv")
heating_types_df: pd.DataFrame = pd.read_csv("fuels_and_heating_collection/tipovi_grejanja.csv")


# BACKEND -> DB (csv file) API

def __db_get_all_fuel_types_lat() -> list[str]:
	fuel_types_lat: list[str] = fuels_df['fuel_type_latin'].tolist()
	
	return fuel_types_lat

def __db_get_all_fuel_types_cyr() -> list[str]:
	fuel_types_cyr: list[str] = fuels_df['fuel_type_cyrillic'].tolist()

	return fuel_types_cyr

# FRONTEND -> BECKEND API

def be_get_all_fuel_types_lat() -> list[str]:	
    return __db_get_all_fuel_types_lat()


def be_get_all_fuel_types_cyr() -> list[str]:	
    return __db_get_all_fuel_types_cyr()

