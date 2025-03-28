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
from fuels_and_heating_collection import fuels_and_heating_types

def fetch_data_and_calculate(general_input: GeneralInputData, solar_input: SolarCollectorsUserInput) -> OutputData:

    month_models: list[months.MonthModel] = months.be_get_all()
    
    Q_nd: float = 0
    total_collector_production: float = 0

    for month_model in month_models:
        # monthly calculations of needed energy and achieved production
        needed_production = calculate_needed_energy_for_period_kWh(month_model.number_of_days, solar_input.number_of_people)
        collector_production = calculate_monthly_captured_heat_kWh(month_model.avg_production_kWh_m2,
                                                                   solar_input.collector_surface_area_m2,
                                                                   solar_input.collector_efficeny)
        if (collector_production > needed_production):
            collector_production = needed_production
        
        Q_nd = Q_nd + needed_production
        total_collector_production = total_collector_production + collector_production


    coeffs = fuels_and_heating_types.be_get_coefficents(solar_input.water_heating_source, "етажно грејање")
    fuel_data = fuels_and_heating_types.be_get_fuel_cyr(solar_input.water_heating_source)
    
    # KOJE KOEFICIJENTE KORISTITI?
    curr_system_efficency_coef = coeffs.fuel_efficency * coeffs.pipe_system_efficency * coeffs.regulation_efficency
    #curr_system_efficency_coef = 0.58*0.95*0.92
    
    delivered_energy_prev: float = Q_nd / curr_system_efficency_coef
    delivered_energy_new: float = (Q_nd-total_collector_production) / curr_system_efficency_coef
    
    curr_yearly_expenses: float = delivered_energy_prev * fuel_data.consumtion_per_kWh * solar_input.energy_source_price_per_unit
    new_yearly_expenses: float = delivered_energy_new * fuel_data.consumtion_per_kWh * solar_input.energy_source_price_per_unit
    
    yearly_savings: float = curr_yearly_expenses - new_yearly_expenses
    payback_period: float = solar_input.investment_price / yearly_savings
    percantage_saved: float = total_collector_production / Q_nd

    return OutputData(curr_yearly_expenses, yearly_savings, payback_period, percantage_saved, total_collector_production)


def test():
    # Example Usage
   
    general_input: GeneralInputData = GeneralInputData(municipality_name_lat="Aleksandrovac", heating_type_lat="etažno")
    
    collector_user_input: SolarCollectorsUserInput = SolarCollectorsUserInput(
        investment_price = 100000,
        water_heating_source = 'дрво',
        energy_source_price_per_unit = 8000,
        number_of_people = 5,
        collector_surface_area_m2 = 2,
        collector_efficeny = 0.6
    )

    output: OutputData = fetch_data_and_calculate(general_input, collector_user_input)
    print(output)

if __name__ == '__main__':
	test()