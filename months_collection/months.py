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

def db_get_all() -> list[MonthModel]:
    
	# TODO

	return []

# FRONTEND -> BECKEND API

def be_get_all() -> list[MonthModel]:
    return db_get_all()
