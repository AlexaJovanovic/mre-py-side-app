from enum import Enum

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

district_names = [
	"Западнобачки",
	"Севернобачки",
	"Севернобанатски",
	"Јужнобачки",
	"Средњeбанатски",
	"Сремски",
	"Јужнобанатски",
	"Мачвански",
	"Београдски",
	"Колубарски",
	"Подунавски",
	"Браничевски",
	"Златиборски",
	"Моравички",
	"Шумадијски",
	"Поморавски",
	"Борски",
	"Рашки",
	"Расински",
	"Нишавски",
	"Зајечарски",
	"Топлички",
	"Јабланички",
	"Пиротски",
	"Пчињски"
]

roof_solar_production_vals = [
	1.175,
	1.179,
	1.178,
	1.184,
	1.185,
	1.177,
	1.187,
	1.169,
	1.186,
	1.162,
	1.178,
	1.183,
	1.228,
	1.178,
	1.182,
	1.187,
	1.227,
	1.196,
	1.188,
	1.224,
	1.247,
	1.231,
	1.22,
	1.248,
	1.268
]

land_solar_production_vals = [
	1.412,
	1.417,
	1.416,
	1.423,
	1.424,
	1.413,
	1.426,
	1.399,
	1.418,
	1.416,
	1.402,
	1.423,
	1.459,
	1.411,
	1.415,
	1.426,
	1.483,
	1.412,
	1.408,
	1.472,
	1.479,
	1.469,
	1.473,
	1.494,
	1.526
]