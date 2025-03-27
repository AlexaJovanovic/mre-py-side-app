import pandas as pd
from dataclasses import dataclass

@dataclass
class CoefficientsModel:
    fuel_efficency: float
    pipe_system_efficency: float
    regulation_efficency: float

@dataclass
class FuelModel:
    fuel_type_latin: str
    fuel_type_cyrillic: str
    prim_en_conv_factor: float
    co2_emission_kg_per_kWh: float
    unit: str
    consumtion_per_kWh: float

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

def __db_get_fuel_lat(fuel_type_lat: str) -> FuelModel:
    fuel_data = fuels_df[fuels_df["fuel_type_latin"] == fuel_type_lat]
    fuel_data = fuel_data.iloc[0]  # Convert to Series
    
    return FuelModel(
            fuel_type_latin=fuel_data["fuel_type_latin"],
            fuel_type_cyrillic=fuel_data["fuel_type_cyrillic"],
            prim_en_conv_factor=float(fuel_data["prim_en_conv_factor"]),
            co2_emission_kg_per_kWh=float(fuel_data["co2_emission_kg_per_kWh"]),
            unit=fuel_data["unit"],
            consumtion_per_kWh=float(fuel_data["consumtion_per_kWh"]),
            )

def __db_get_fuel_cyr(fuel_type_cyr: str) -> FuelModel:
    fuel_data = fuels_df[fuels_df["fuel_type_cyrillic"] == fuel_type_cyr]
    fuel_data = fuel_data.iloc[0]  # Convert to Series
    
    return FuelModel(
            fuel_type_latin=fuel_data["fuel_type_latin"],
            fuel_type_cyrillic=fuel_data["fuel_type_cyrillic"],
            prim_en_conv_factor=float(fuel_data["prim_en_conv_factor"]),
            co2_emission_kg_per_kWh=float(fuel_data["co2_emission_kg_per_kWh"]),
            unit=fuel_data["unit"],
            consumtion_per_kWh=float(fuel_data["consumtion_per_kWh"]),
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

def be_get_fuel_lat(fuel_type_lat: str) -> FuelModel:
    return __db_get_fuel_lat(fuel_type_lat)

def be_get_fuel_cyr(fuel_type_cyr: str) -> FuelModel:
    return __db_get_fuel_cyr(fuel_type_cyr)