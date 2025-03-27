from dataclasses import dataclass

@dataclass
class GeneralInputData:
    municipality_name_lat: str
    heating_type_lat: str
    
        
@dataclass
class OutputData:
    curr_yearly_expenses: float # Estimate for the current expenses for energy
    yearly_savings: float  # Total saved energy costs
    payback_period: float  # Years to recover the investment
    percantage_saved: float # What percentage of energy will be saved

    saved_delivered_energy: float = -1 # VEROVTNO SE NECE KORISTITI  
    price_for_saving_1kwh: float = -1 # VEROVTNO SE NECE KORISTITI  

NOT_PROVIDED: float = -1

