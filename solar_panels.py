from dataclasses import dataclass
from enum import Enum


# Dve opcije za mesto instalacije solarnih panela
class SolarPanelLocation(Enum):
    ROOF = "krov"
    LAND = "u okucnici"

# Informacije koje se dodatno unose za meru solarnih panela 
@dataclass
class SolarPanelsUserInput:
    yearly_electricity_consumption: float
    electricity_price_per_kwh: float
    location: SolarPanelLocation

@dataclass
class OutputData:
    curr_yearly_expenses: float # Estimate for the current expenses for energy
    yearly_savings: float  # Total saved energy costs
    payback_period: float  # Years to recover the investment
    percantage_saved: float # What percentage of energy will be saved

    saved_delivered_energy: float = -1 # VEROVTNO SE NECE KORISTITI  
    price_for_saving_1kwh: float = -1 # VEROVTNO SE NECE KORISTITI  

NOT_PROVIDED: float = -1

import municipalities as mp
import districts as dt

def calc_for_solar_panels(
        municipality: mp.SrbMunicipalities,
        user_input: SolarPanelsUserInput, 
        investment_price: float = NOT_PROVIDED, 
        power_installed: float = NOT_PROVIDED,
        ) -> OutputData:
    
    if (investment_price == NOT_PROVIDED or power_installed == NOT_PROVIDED):
        # AKO SE NE SPECIFICIRA CENA IZGRADNJE I PLANIRANA SNAGA
        # ONDA NE MOGU DA SE SRACUNAJU IZLAZNI PARAMETRI
        # ALI MOZE DA SE PREPORUCI KOLIKA SNAGA BI ZADOVOLJILA 100% potreba
        my_district = mp.corresponding_districts[municipality.value]
        
        recommended_power_to_install: float
        
        if (user_input.location == SolarPanelLocation.ROOF):
            recommended_power_to_install = user_input.yearly_electricity_consumption / dt.roof_solar_production[my_district.value] / 1000
        elif (user_input.location == SolarPanelLocation.LAND):
            recommended_power_to_install = user_input.yearly_electricity_consumption / dt.land_solar_production[my_district.value] / 1000

        print(f'Maskimalna snaga koja treba da se ugradi da bi se pokrili svi troskovi je: {recommended_power_to_install}kWp')
        
        return None

    curr_yearly_expenses = user_input.yearly_electricity_consumption * user_input.electricity_price_per_kwh
    
    my_district = mp.corresponding_districts[municipality.value]
    my_yearly_production : float = power_installed * dt.land_solar_production[my_district.value] * 1000
    
    percantage_saved = my_yearly_production / user_input.yearly_electricity_consumption * 100
    yearly_savings = my_yearly_production * user_input.electricity_price_per_kwh
    payback_period = investment_price / yearly_savings

    return OutputData(curr_yearly_expenses, yearly_savings, payback_period, percantage_saved)
    
# Example Usage
user_data = SolarPanelsUserInput(
    yearly_electricity_consumption=7000.0,
    electricity_price_per_kwh=10,
    location=SolarPanelLocation.LAND
)

print(user_data)

output = calc_for_solar_panels(municipality=mp.SrbMunicipalities.ALIBUNAR, user_input=user_data)

output = calc_for_solar_panels(municipality=mp.SrbMunicipalities.ALIBUNAR, user_input=user_data, investment_price=200_000.0, power_installed=4)
print("\nRacunca:\n", output)
