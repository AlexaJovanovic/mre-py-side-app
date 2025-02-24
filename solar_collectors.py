from output_data_struct import OutputData
from output_data_struct import NOT_PROVIDED
import municipalities as mp



def calc_for_solar_collectors(
        municipality: mp.SrbMunicipalities,
        investment_price: float = NOT_PROVIDED, 
        power_installed: float = NOT_PROVIDED,
        ) -> OutputData:
    
    efficency_coefficent: float = -1 # VLOOKUP(B255,B52:J59,9,FALSE)
    needed_energy: float = -1 
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
    