from output_data_struct import OutputData
from output_data_struct import NOT_PROVIDED
import municipalities as mp



def calc_for_solar_collectors(
        municipality: mp.SrbMunicipalities,
        investment_price: float = NOT_PROVIDED, 
        power_installed: float = NOT_PROVIDED,
        ) -> OutputData:
    
    if (investment_price == NOT_PROVIDED or power_installed == NOT_PROVIDED):
        # AKO SE NE SPECIFICIRA CENA IZGRADNJE I PLANIRANA SNAGA
        # ONDA NE MOGU DA SE SRACUNAJU IZLAZNI PARAMETRI
        # ALI MOZE DA SE PREPORUCI POVRSINA KOLEKTORA KOJA BI ZADOVOLJILA 
        # 100% POTREBA ZA TOPLOM VODOM

        my_district = mp.corresponding_districts[municipality.value]
        
        recommended_power_to_install: float
        
        print(f'Maskimalna povrsina kolektora koja treba da se ugradi da bi se pokrili troskovi tople vode je: {recommended_power_to_install}m^2')
        
        return None

    return OutputData(NOT_PROVIDED, NOT_PROVIDED, NOT_PROVIDED, NOT_PROVIDED)
    