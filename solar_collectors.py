from general_data_structs import OutputData
from general_data_structs import NOT_PROVIDED
import municipalities_collection.municipalities as mp
from dataclasses import dataclass

# USVOJENE KONSTANTE
WATER_DENSITY: float = 985 # kg/m^3 at temp
WATER_HEAT_CAPACITY: float = 4.2 # kJ/(kg*K)
SUPPLY_WATER_TEMP: float = 10 # deg C
DESIRED_WATER_TEMP: float = 35 # deg C
NEEDED_WARM_WATER_VOLUME: float = 30 # liters per day per person

# Informacije koje se dodatno unose za meru solarnih panela 
@dataclass
class SolarCollectorsUserInput:
    investment_price: float
    water_heating_source: str
    energy_source_price_per_unit: float
    number_of_people: int
    collector_surface_area_m2: float
    collector_efficeny: float

# calc needed energy for one person
needed_energy_in_kJ = (NEEDED_WARM_WATER_VOLUME / 1000)*WATER_DENSITY*WATER_HEAT_CAPACITY*(DESIRED_WATER_TEMP - SUPPLY_WATER_TEMP)
needed_energy_in_kWh = needed_energy_in_kJ / 3600
num_of_persons = 4
num_of_days = 31
print(needed_energy_in_kWh*num_of_persons*num_of_days)

# calc for produced energy
solar_power_base_on_month: float = 39 # kWh/m^2 per day CITA SE IZ TABELE O MESECIMA
solar_collector_surface_area: float = 2 # m^2 USER INPUT
collector_efficeny: float = 0.6 # USER INPUT
produced_heat = solar_power_base_on_month * solar_collector_surface_area * collector_efficeny


def calc_for_solar_collectors(
        municipality: mp.SrbMunicipalities,
        investment_price: float = NOT_PROVIDED, 
        power_installed: float = NOT_PROVIDED,
        ) -> OutputData:
    
    # UNOS!K21 JE TRUE AKO SE PRIMENJUJE MERA KOLEKTORA
    
    efficency_coefficent: float = -1 # VLOOKUP(B255,B52:J59,9,FALSE)
    needed_energy: float = 0 # racuna se kao suma po svim mesecima
    energy_consumption_for_water_heating : float = needed_energy / efficency_coefficent
    energy_price_per_kwh: float = -1
    
    curr_yearly_expenses = energy_consumption_for_water_heating * energy_price_per_kwh

    if (investment_price == NOT_PROVIDED or power_installed == NOT_PROVIDED):
        # AKO SE NE SPECIFICIRA CENA IZGRADNJE I PLANIRANA SNAGA
        # ONDA NE MOGU DA SE SRACUNAJU IZLAZNI PARAMETRI
        # ALI MOZE DA SE PREPORUCI POVRSINA KOLEKTORA KOJA BI ZADOVOLJILA 
        # 100% POTREBA ZA TOPLOM VODOM

        my_district = mp.corresponding_districts[municipality.value]
        
        recommended_surface_area: float = 0
        
        print(f'Maskimalna povrsina kolektora koja treba da se ugradi da bi se pokrili troskovi tople vode je: {recommended_surface_area}m^2')
        
        return None

    return OutputData(NOT_PROVIDED, NOT_PROVIDED, NOT_PROVIDED, NOT_PROVIDED)
    