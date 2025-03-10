from enum import Enum
import pandas as pd
from dataclasses import dataclass

@dataclass
class DistrictModel:
    name_latin: str
    name_cyrillic: str
    roof_production_MWh_MWp: float
    land_production_MWh_MWp: float

class SrbDistricts(Enum):
	ZAPADNOBACKI = 0
	SEVERNOBACKI = 1
	SEVERNOBANATSKI = 2
	JUZNOBACKI = 3
	SREDNJEBANATSKI = 4
	SREMSKI = 5
	JUZNOBANATSKI = 6
	MACVANSKI = 7
	BEOGRADSKI = 8
	KOLUBARSKI = 9
	PODUNAVSKI = 10
	BRANICEVSKI = 11
	ZLATIBORSKI = 12
	MORAVICKI = 13
	SUMADIJSKI = 14
	POMORAVSKI = 15
	BORSKI = 16
	RASKI = 17
	RASINSKI = 18
	NISAVSKI = 19
	ZAJECARSKI = 20
	TOPLICKI = 21
	JABLANICKI = 22
	PIROTSKI = 23
	PCINJSKI = 24


districts_df: pd.DataFrame = pd.read_csv("districts_collection/okruzi.csv")

# BACKEND -> DB (csv file) API

def __db_get_all() -> list[DistrictModel]:
	districts: list[DistrictModel] = []
	
	for _, row in districts_df.iterrows():
		d_model: DistrictModel = DistrictModel(
			row['name_latin'],
			row['name_cyrillic'],
			row['roof_production_MWh_MWp'],
			row['land_production_MWh_MWp']
		)
		
		districts.append(d_model)

	return districts

def __db_get_by_name_lat(district_name_lat: str) -> DistrictModel:
	row = districts_df[districts_df['name_latin'] == district_name_lat]
	
	if row.empty:
		return None
	
	row = row.iloc[0]
	d_model: DistrictModel = DistrictModel(
			row['name_latin'],
			row['name_cyrillic'],
			float(row['roof_production_MWh_MWp']),
			float(row['land_production_MWh_MWp'])
		)
	
	return d_model

def __db_get_by_name_cyr(district_name_cyr: str) -> DistrictModel:
	row = districts_df[districts_df['name_cyrillic'] == district_name_cyr]
	
	if row.empty:
		return None
	
	row = row.iloc[0]
	d_model: DistrictModel = DistrictModel(
			row['name_latin'],
			row['name_cyrillic'],
			float(row['roof_production_MWh_MWp']),
			float(row['land_production_MWh_MWp'])
		)
	
	return d_model


# FRONTEND -> BECKEND API

def be_get_all() -> list[DistrictModel]:	
    return __db_get_all()

def be_get_by_name_lat(district_name_lat: str) -> DistrictModel:
	return __db_get_by_name_lat(district_name_lat)

def be_get_by_name_cyr(district_name_cyr: str) -> DistrictModel:
	return __db_get_by_name_cyr(district_name_cyr)

def test():
	d_list = be_get_all()

	for d in d_list:
		print(d)

	d = d_list[4]

	print(f'Searching for {d.name_latin}:{d.name_cyrillic}')

	dd = be_get_by_name_lat(d.name_latin)
	print(dd)
	dd = be_get_by_name_lat('Nonexistant')
	print(dd)

if __name__ == '__main__':
	test()
