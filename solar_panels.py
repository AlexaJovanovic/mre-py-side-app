from dataclasses import dataclass
from enum import Enum
from general_data_structs import OutputData
from general_data_structs import GeneralInputData
from general_data_structs import NOT_PROVIDED

# Dve opcije za mesto instalacije solarnih panela
class SolarPanelLocation(Enum):
    ROOF = "krov"
    LAND = "u okucnici"

# Informacije koje se dodatno unose za meru solarnih panela 
@dataclass
class SolarPanelsUserInput:
    investment_price: float
    yearly_electricity_consumption: float
    electricity_price_per_kwh: float
    location: SolarPanelLocation
    installed_power_kWp: float

import municipalities_collection.municipalities as mp
import districts_collection.districts as dt

def calculate_recommended_power_to_install(
        yearly_electricity_consumption_kWh: float,
        el_production_MWh_kWp: float
        ) -> float:
    recommended_power_to_install_kWp: float
    
    recommended_power_to_install_kWp = yearly_electricity_consumption_kWh / 1000 / el_production_MWh_kWp

    return recommended_power_to_install_kWp

def calculate_yeraly_production_in_kWh(power_installed_kWp: float, el_production_MWh_kWp: float) -> float:
    yearly_production_kWh : float = power_installed_kWp * el_production_MWh_kWp * 1000
    return yearly_production_kWh
    
def calculation_for_solar_panels(
        yearly_electricity_consumption_kWh: float, 
        electricity_price_per_kWh: float,
        investment_price: float, 
        power_installed_kWp: float,
        el_production_MWh_kWp: float
        ) -> OutputData:

    curr_yearly_expenses: float = yearly_electricity_consumption_kWh * electricity_price_per_kWh
    my_yearly_production_kWh : float = calculate_yeraly_production_in_kWh(power_installed_kWp, el_production_MWh_kWp)

    percantage_saved: float = my_yearly_production_kWh / yearly_electricity_consumption_kWh * 100
    yearly_savings: float = my_yearly_production_kWh * electricity_price_per_kWh
    payback_period = investment_price / yearly_savings

    return OutputData(curr_yearly_expenses, yearly_savings, payback_period, percantage_saved)

def fetch_data_and_calculate(general_input: GeneralInputData, solar_input: SolarPanelsUserInput) -> OutputData:
    mun_name_lat = general_input.municipality_name_lat

    municipality: mp.MunicipalityModel = mp.be_get_by_name_lat(mun_name_lat)
    district: dt.DistrictModel = dt.be_get_by_name_lat(municipality.district_latin)

    production_MWh_kWp : float
    if (solar_input.location == SolarPanelLocation.LAND):
        production_MWh_kWp = district.land_production_MWh_MWp
    else:
        production_MWh_kWp = district.roof_production_MWh_MWp

    results: OutputData = calculation_for_solar_panels(solar_input.yearly_electricity_consumption,
                                                        solar_input.electricity_price_per_kwh,
                                                        solar_input.investment_price,
                                                        solar_input.installed_power_kWp,
                                                        production_MWh_kWp)
    
    return results

def test():
    # Example Usage
    general_input: GeneralInputData = GeneralInputData(municipality_name_lat="Aleksandrovac", heating_type_lat=None)
    solar_user_input: SolarPanelsUserInput = SolarPanelsUserInput(
        investment_price=600000,
        yearly_electricity_consumption=8000.0,
        electricity_price_per_kwh=10,
        location=SolarPanelLocation.LAND, 
        installed_power_kWp=5
    )

    output: OutputData = fetch_data_and_calculate(general_input, solar_user_input)
    print(output)

if __name__ == '__main__':
	test()