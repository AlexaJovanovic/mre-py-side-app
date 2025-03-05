from enum import Enum
import pandas as pd
from dataclasses import dataclass


@dataclass
class MonthModel:
    name_latin: str
    name_cyrillic: str
    number_of_days: int
    avg_production_kWh_m2: float


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

months_df: pd.DataFrame = pd.read_csv("months_collection/months.csv")

days_column = 'number_of_days'
cyrilic_names_column = 'name_cyrillic'
average_energy_column = 'avg_production_kWh_m2'


# BACKEND -> DB (csv file) API

def __db_get_all() -> list[MonthModel]:
	months: list[MonthModel] = []
    
	for m in Months:
		row = months_df.iloc[m.value]
		model = MonthModel(row['name_latin'], row['name_cyrillic'], row['number_of_days'], row['avg_production_kWh_m2'])
		
		months.append(model)

	return months

# FRONTEND -> BECKEND API

def be_get_all() -> list[MonthModel]:	
    return __db_get_all()

def test():
	m_list = be_get_all()

	for m in m_list:
		print(m)
