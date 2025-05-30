from enum import Enum
import pandas as pd
from dataclasses import dataclass

@dataclass
class MunicipalityModel:
    name_latin: str
    name_cyrillic: str
    HDD: float
    district_latin: str
    district_cyrillic: str

class SrbMunicipalities(Enum):
	ADA = 0
	ALEKSANDROVAC = 1
	ALEKSINAC = 2
	ALIBUNAR = 3
	APATIN = 4
	ARANDJELOVAC = 5
	ARILJE = 6
	BABUSNICA = 7
	BAJINA_BASTA = 8
	BARAJEVO = 9
	BATOCINA = 10
	BAC = 11
	BACKA_TOPOLA = 12
	BACKI_PETROVAC = 13
	BELA_PALANKA = 14
	BELA_CRKVA = 15
	BEOCIN = 16
	BECEJI = 17
	BLACE = 18
	BOGATIC = 19
	BOJNIK = 20
	BOJLEVAC = 21
	BOR = 22
	BOSILEGRAD = 23
	BRUS = 24
	BUJANOVAC = 25
	VALJEVO = 26
	VARVARIN = 27
	VELIKA_PLANA = 28
	VELIKO_GRADISTE = 29
	VLADIMIRCI = 30
	VLADICIN_HAN = 31
	VLASOTINCE = 32
	VOZDOVAC = 33
	VRANJE = 34
	VRACAR = 35
	VRBAS = 36
	VRNJACKA_BANJA = 37
	VRSAC = 38
	GNJILANE = 39
	GOLUBAC = 40
	GORNJI_MILANOVAC = 41
	GROCKA = 42
	DESPOTOVAC = 43
	DIMITROVGRAD = 44
	ZABALJ = 45
	ZABARI = 46
	ZAGUBICA = 47
	ZITISTE = 48
	ZITORADJA = 49
	ZAJECAR = 50
	ZVEZDARA = 51
	ZEMUN = 52
	ZRENJANIN = 53
	IVANJICA = 54
	INDIJA = 55
	IRIG = 56
	KANJIZA = 57
	KIKINDA = 58
	KLADOVO = 59
	KNIC = 60
	KNJAZEVAC = 61
	KOVACICA = 62
	KOVIN = 63
	KOSJERIC = 64
	KOSOVSKA_MITROVICA = 65
	KOCEJEVA = 66
	KRAGUJEVAC = 67
	KRALJEVO = 68
	KRUPANJ = 69
	KRUSEVAC = 70
	KULA = 71
	KURSUMLIJA = 72
	KUCEVO = 73
	LAZAREVAC = 74
	LAJKOVAC = 75
	LAPOVO = 76
	LEBANE = 77
	LESKOVAC = 78
	LOZNICA = 79
	LUCANI = 80
	LJUBOVIJA = 81
	MAJDANPEK = 82
	MALI_ZVORNIK = 83
	MALI_IDOS = 84
	MALO_CRNICE = 85
	MEDVEDA = 86
	MEROSINA = 87
	MIIONICA = 88
	MLADENOVAC = 89
	NEGOTIN = 90
	NIS = 91
	NOVA_VAROS = 92
	NOVA_CRNJA = 93
	NOVI_BEOGRAD = 94
	NOVI_BECEJ = 95
	NOVI_KNEZEVAC = 96
	NOVI_PAZAR = 97
	NOVI_SAD = 98
	OBRENOVAC = 99
	OPOVO = 100
	ODZACI = 101
	PALILULA = 102
	PANCEVO = 103
	PARACIN = 104
	PETROVAC_NA_MLAVI = 105
	PECINCI = 106
	PIROT = 107
	PLANDISTE = 108
	POZAREVAC = 109
	POZEGA = 110
	PRESEVO = 111
	PRIBOJ = 112
	PRIJEPOLJE = 113
	PROKUPJE = 114
	RAKOVICA = 115
	RACA = 116
	RASKA = 117
	SAVSKI_VENAC = 118
	SVILAJNAC = 119
	SENTA = 120
	SECANJ = 121
	SMEDEREVO = 122
	SMEDEREVSKA_PALANKA = 123
	SOKOBANJA = 124
	SOMBOR = 125
	SRBOBRAN = 126
	SREMSKA_MITROVICA = 127
	SREMSKI_KARLOVCI = 128
	STARA_PAZOVA = 129
	STARI_GRAD = 130
	SUBOTICA = 131
	SURCIN = 132
	TEMERIN = 133
	TITEL = 134
	TOPOLA = 135
	TRGOVISTE = 136
	TRSTENIK = 137
	TUTIN = 138
	CUPRIJA = 139
	UZICE = 140
	CAJETINA = 141
	CACAK = 142
	COKA = 143
	SABAC = 144
	SID = 145

municipalities_df: pd.DataFrame = pd.read_csv("municipalities_collection/Opstine.csv")

# BACKEND -> DB (csv file) API

def __db_get_all() -> list[MunicipalityModel]:
	districts: list[MunicipalityModel] = []
	
	for _, row in municipalities_df.iterrows():
		d_model: MunicipalityModel = MunicipalityModel(
			row['name_latin'],
			row['name_cyrillic'],
			row['HDD'],
			row['district_latin'],
			row['district_cyrillic']
		)
		
		districts.append(d_model)

	return districts

def __db_get_by_name_lat(district_name_lat: str) -> MunicipalityModel:
	row = municipalities_df[municipalities_df['name_latin'] == district_name_lat]
	
	if row.empty:
		return None
	
	row = row.iloc[0]
	d_model: MunicipalityModel = MunicipalityModel(
			row['name_latin'],
			row['name_cyrillic'],
			float(row['HDD']),
			row['district_latin'],
			row['district_cyrillic']
		)
	
	return d_model

def __db_get_by_name_cyr(district_name_cyr: str) -> MunicipalityModel:
	row = municipalities_df[municipalities_df['name_cyrillic'] == district_name_cyr]
	
	if row.empty:
		return None
	
	row = row.iloc[0]
	d_model: MunicipalityModel = MunicipalityModel(
			row['name_latin'],
			row['name_cyrillic'],
			float(row['HDD']),
			row['district_latin'],
			row['district_cyrillic']
		)
	
	return d_model

# FRONTEND -> BECKEND API

def be_get_all() -> list[MunicipalityModel]:	
    return __db_get_all()

def be_get_by_name_lat(district_name_lat: str) -> MunicipalityModel:
	return __db_get_by_name_lat(district_name_lat)

def be_get_by_name_cyr(district_name_cyr: str) -> MunicipalityModel:
	return __db_get_by_name_cyr(district_name_cyr)

def test():
	m_list = be_get_all()

	for m in m_list:
		print(m)

	d = m_list[4]

	print(f'Searching for {m.name_latin}:{m.name_cyrillic}')

	mm = be_get_by_name_lat(m.name_latin)
	print(mm)
	mm = be_get_by_name_lat('Nonexistant')
	print(mm)

if __name__ == '__main__':
	test()
