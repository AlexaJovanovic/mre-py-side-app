from dataclasses import dataclass
from enum import Enum

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

@dataclass
class OutputData:
    curr_yearly_expenses: float # Estimate of the current expenses for energy
    yearly_savings: float  # Total saved energy costs
    payback_period: float  # Years to recover the investment
    percantage_saved: float # What percentage of energy will be saved

    saved_delivered_energy: float = -1 # VEROVTNO SE NECE KORISTITI  
    price_for_saving_1kwh: float = -1 # VEROVTNO SE NECE KORISTITI  

# Example Usage
user_data = SolarPanelsUserInput(
    investment_price=10000.0,
    yearly_electricity_consumption=5000.0,
    electricity_price_per_kwh=0.15,
    location=SolarPanelLocation.LAND
)

print(user_data)

