from general_data_structs import OutputData
from general_data_structs import NOT_PROVIDED
from general_data_structs import GeneralInputData
import municipalities_collection.municipalities as mp
from dataclasses import dataclass

# USVOJENE KONSTANTE
WATER_DENSITY: float = 985 # kg/m^3 at temp
WATER_HEAT_CAPACITY: float = 4.2 # kJ/(kg*K)
SUPPLY_WATER_TEMP: float = 10 # deg C
DESIRED_WATER_TEMP: float = 35 # deg C
NEEDED_WARM_WATER_VOLUME_L: float = 30 # liters per day per person

# constant needed energy for one person for one day
NEEDED_ENERGY_PER_PERSON_IN_KJ: float = (NEEDED_WARM_WATER_VOLUME_L / 1000)*WATER_DENSITY*WATER_HEAT_CAPACITY*(DESIRED_WATER_TEMP - SUPPLY_WATER_TEMP)
NEEDED_ENERGY_PER_PERSON_IN_KWH = NEEDED_ENERGY_PER_PERSON_IN_KJ / 3600

# Informacije koje se dodatno unose za meru solarnih kolektora 
@dataclass
class SolarCollectorsUserInput:
    investment_price: float
    water_heating_source: str
    energy_source_price_per_unit: float
    number_of_people: int
    collector_surface_area_m2: float
    collector_efficeny: float

def calculate_needed_energy_for_period_kWh(num_of_days: float, num_of_persons: float) -> float:
    Q_nd: float = NEEDED_ENERGY_PER_PERSON_IN_KWH * num_of_days * num_of_persons
    
    return Q_nd

def calculate_monthly_captured_heat_kWh(monthly_sun_energy_kWh_m2: float,
                                             collector_surface_area_m2: float,
                                             collector_efficency: float) -> float:
    
    captured_heat_kWh: float = monthly_sun_energy_kWh_m2 * collector_surface_area_m2 * collector_efficency
    
    return captured_heat_kWh

from months_collection import months

def fetch_data_and_calculate(general_input: GeneralInputData, solar_input: SolarCollectorsUserInput) -> OutputData:

    month_models: list[months.MonthModel] = months.be_get_all()
    
    efficency_coefficent: float = -1 # VLOOKUP(B255,B52:J59,9,FALSE)
    needed_energy: float = 0 # racuna se kao suma po svim mesecima
    energy_consumption_for_water_heating : float = needed_energy / efficency_coefficent
    energy_price_per_kwh: float = -1
    
    curr_yearly_expenses = energy_consumption_for_water_heating * energy_price_per_kwh

    return OutputData(NOT_PROVIDED, NOT_PROVIDED, NOT_PROVIDED, NOT_PROVIDED)
    