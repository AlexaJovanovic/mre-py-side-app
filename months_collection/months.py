from enum import Enum
import pandas as pd

class Months(Enum):
	JANUAR = 0
	FEBRAUR = 1
	MART = 2
	APRIL = 3
	MAJ = 4
	JUN = 5
	JUL = 6
	AVGUST = 7
	SEPTEMBAR = 8
	OKTOBAR = 9
	NOVEMBAR = 10
	DECEMBAR = 11

months_df: pd.DataFrame = pd.read_csv("months.csv")

days_column = 'broj dana'
cyrilic_names_column = 'cirilica'
average_energy_column = 'prosek(kWh/m2)'

def get_number_of_days_in_a_month(month: Months) -> int:
    return months_df[days_column][month.value]

def get_months_name_cyrilic(month: Months) -> str:
    return months_df[cyrilic_names_column][month.value]

def get_average_energy_from_sun_per_m2_in_month(month: Months) -> str:
    return months_df[average_energy_column][month.value]

