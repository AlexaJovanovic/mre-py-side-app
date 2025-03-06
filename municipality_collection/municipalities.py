from enum import Enum

from districts_collection.districts import *

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

municipality_names = [
	"Ада",
	"Александровац",
	"Алексинац",
	"Алибунар",
	"Апатин",
	"Аранђеловац",
	"Ариље",
	"Бабушница",
	"Бајина Башта",
	"Барајево",
	"Баточина",
	"Бач",
	"Бачка Топола",
	"Бачки Петровац",
	"Бела Паланка",
	"Бела Црква",
	"Беочин",
	"Бечеј",
	"Блаце",
	"Богатић",
	"Бојник",
	"Бољевац",
	"Бор",
	"Босилеград",
	"Брус",
	"Бујановац",
	"Ваљево",
	"Варварин",
	"Велика Плана",
	"Велико Градиште",
	"Владимирци",
	"Владичин Хан",
	"Власотинце",
	"Вождовац",
	"Врање",
	"Врачар",
	"Врбас",
	"Врњачка Бања",
	"Вршац",
	"Гњилане",
	"Голубац",
	"Горњи Милановац",
	"Гроцка",
	"Деспотовац",
	"Димитровград",
	"Жабаљ",
	"Жабари",
	"Жагубица",
	"Житиште",
	"Житорађа",
	"Зајечар",
	"Звездара",
	"Земун",
	"Зрењанин",
	"Ивањица",
	"Инђија",
	"Ириг",
	"Кањижа",
	"Кикинда",
	"Кладово",
	"Кнић",
	"Књажевац",
	"Ковачица",
	"Ковин",
	"Косјерић",
	"Косовска Митровица",
	"Коцељева",
	"Крагујевац",
	"Краљево",
	"Крупањ",
	"Крушевац",
	"Кула",
	"Куршумлија",
	"Кучево",
	"Лазаревац",
	"Лајковац",
	"Лапово",
	"Лебане",
	"Лесковац",
	"Лозница",
	"Лучани",
	"Љубовија",
	"Мајданпек",
	"Мали Зворник",
	"Мали Иђош",
	"Мало Црниће",
	"Медвеђа",
	"Мерошина",
	"Мионица",
	"Младеновац",
	"Неготин",
	"Ниш",
	"Нова Варош",
	"Нова Црња",
	"Нови Београд",
	"Нови Бечеј",
	"Нови Кнежевац",
	"Нови Пазар",
	"Нови Сад",
	"Обреновац",
	"Опово",
	"Оџаци",
	"Палилула",
	"Панчево",
	"Параћин",
	"Петровац на Млави",
	"Пећинци",
	"Пирот",
	"Пландиште",
	"Пожаревац",
	"Пожега",
	"Прешево",
	"Прибој",
	"Пријепоље",
	"Прокупље",
	"Раковица",
	"Рача",
	"Рашка",
	"Савски Венац",
	"Свилајнац",
	"Сента",
	"Сечањ",
	"Смедерево",
	"Смедеревска Паланка",
	"Сокобања",
	"Сомбор",
	"Србобран",
	"Сремска Митровица",
	"Сремски Карловци",
	"Стара Пазова",
	"Стари Град",
	"Суботица",
	"Сурчин",
	"Темерин",
	"Тител",
	"Топола",
	"Трговиште",
	"Трстеник",
	"Тутин",
	"Ћуприја",
	"Ужице",
	"Чајетина",
	"Чачак",
	"Чока",
	"Шабац",
	"Шид"
]
municipality_HDDs = [
	2644.2,
	2588.6,
	2476.7,
	2596.4,
	2686.2,
	2554.6,
	3062.0,
	2613.1,
	2627.9,
	2299.0,
	2530.9,
	2604.2,
	2686.2,
	2604.2,
	2613.1,
	2521.0,
	2604.2,
	2604.2,
	2823.3,
	2628.9,
	2681.2,
	2792.3,
	2792.3,
	2662.9,
	3008.5,
	2662.9,
	2557.6,
	2530.9,
	2554.6,
	2629.5,
	2478.7,
	2662.9,
	2681.2,
	2299.0,
	2662.9,
	2299.0,
	2604.2,
	2579.4,
	2521.0,
	2662.9,
	2629.5,
	3062.0,
	2299.0,
	2666.2,
	2957.7,
	2604.2,
	2554.6,
	4049.0,
	2589.7,
	2476.7,
	2792.3,
	2299.0,
	2299.0,
	2589.7,
	2579.4,
	2604.2,
	2628.9,
	2779.2,
	2644.2,
	2567.9,
	2530.9,
	2792.3,
	2596.4,
	2596.4,
	3062.0,
	2823.3,
	2557.6,
	2530.9,
	2579.4,
	2956.4,
	2588.6,
	2686.2,
	2823.3,
	2629.5,
	2299.0,
	2557.6,
	2554.6,
	2681.2,
	2681.2,
	2478.7,
	3062.0,
	2627.9,
	2567.9,
	2478.7,
	2779.2,
	2629.5,
	2823.3,
	2476.7,
	2557.6,
	2554.6,
	2567.9,
	2476.7,
	3956.0,
	2644.2,
	2299.0,
	2644.2,
	2644.2,
	3008.5,
	2604.2,
	2482.5,
	2589.7,
	2686.2,
	2299.0,
	2596.4,
	2666.2,
	2629.5,
	2482.5,
	2613.1,
	2521.0,
	2629.5,
	3062.0,
	2662.9,
	3190.6,
	3190.6,
	2823.3,
	2299.0,
	2530.9,
	3008.5,
	2299.0,
	2666.2,
	2779.2,
	2589.7,
	2554.6,
	2554.6,
	2476.7,
	2686.2,
	2604.2,
	2628.9,
	2604.2,
	2482.5,
	2299.0,
	2779.2,
	2299.0,
	2604.2,
	2589.7,
	2554.6,
	2662.9,
	2588.6,
	3956.0,
	2666.2,
	3062.0,
	3633.9,
	3062.0,
	2644.2,
	2478.7,
	2628.9
]
corresponding_districts = [
	SrbDistricts.SEVERNOBANATSKI,
	SrbDistricts.RASINSKI,
	SrbDistricts.NISAVSKI,
	SrbDistricts.JUZNOBANATSKI,
	SrbDistricts.ZAPADNOBACKI,
	SrbDistricts.SUMADIJSKI,
	SrbDistricts.ZLATIBORSKI,
	SrbDistricts.PIROTSKI,
	SrbDistricts.ZLATIBORSKI,
	SrbDistricts.BEOGRADSKI,
	SrbDistricts.SUMADIJSKI,
	SrbDistricts.JUZNOBACKI,
	SrbDistricts.SEVERNOBACKI,
	SrbDistricts.JUZNOBACKI,
	SrbDistricts.PIROTSKI,
	SrbDistricts.JUZNOBANATSKI,
	SrbDistricts.JUZNOBACKI,
	SrbDistricts.JUZNOBACKI,
	SrbDistricts.TOPLICKI,
	SrbDistricts.MACVANSKI,
	SrbDistricts.JABLANICKI,
	SrbDistricts.ZAJECARSKI,
	SrbDistricts.BORSKI,
	SrbDistricts.PCINJSKI,
	SrbDistricts.RASINSKI,
	SrbDistricts.PCINJSKI,
	SrbDistricts.KOLUBARSKI,
	SrbDistricts.RASINSKI,
	SrbDistricts.PODUNAVSKI,
	SrbDistricts.BRANICEVSKI,
	SrbDistricts.MACVANSKI,
	SrbDistricts.PCINJSKI,
	SrbDistricts.JABLANICKI,
	SrbDistricts.BEOGRADSKI,
	SrbDistricts.PCINJSKI,
	SrbDistricts.BEOGRADSKI,
	SrbDistricts.JUZNOBACKI,
	SrbDistricts.RASKI,
	SrbDistricts.JUZNOBANATSKI,
	SrbDistricts.PCINJSKI,
	SrbDistricts.BRANICEVSKI,
	SrbDistricts.MORAVICKI,
	SrbDistricts.BEOGRADSKI,
	SrbDistricts.POMORAVSKI,
	SrbDistricts.PIROTSKI,
	SrbDistricts.JUZNOBACKI,
	SrbDistricts.BRANICEVSKI,
	SrbDistricts.BRANICEVSKI,
	SrbDistricts.SREDNJEBANATSKI,
	SrbDistricts.TOPLICKI,
	SrbDistricts.ZAJECARSKI,
	SrbDistricts.BEOGRADSKI,
	SrbDistricts.BEOGRADSKI,
	SrbDistricts.SREDNJEBANATSKI,
	SrbDistricts.MORAVICKI,
	SrbDistricts.SREMSKI,
	SrbDistricts.SREMSKI,
	SrbDistricts.SEVERNOBANATSKI,
	SrbDistricts.SEVERNOBANATSKI,
	SrbDistricts.BORSKI,
	SrbDistricts.SUMADIJSKI,
	SrbDistricts.ZAJECARSKI,
	SrbDistricts.JUZNOBANATSKI,
	SrbDistricts.JUZNOBANATSKI,
	SrbDistricts.ZLATIBORSKI,
	SrbDistricts.TOPLICKI,
	SrbDistricts.MACVANSKI,
	SrbDistricts.SUMADIJSKI,
	SrbDistricts.RASKI,
	SrbDistricts.MACVANSKI,
	SrbDistricts.RASINSKI,
	SrbDistricts.ZAPADNOBACKI,
	SrbDistricts.TOPLICKI,
	SrbDistricts.BRANICEVSKI,
	SrbDistricts.BEOGRADSKI,
	SrbDistricts.KOLUBARSKI,
	SrbDistricts.SUMADIJSKI,
	SrbDistricts.JABLANICKI,
	SrbDistricts.JABLANICKI,
	SrbDistricts.MACVANSKI,
	SrbDistricts.MORAVICKI,
	SrbDistricts.MACVANSKI,
	SrbDistricts.BORSKI,
	SrbDistricts.MACVANSKI,
	SrbDistricts.SEVERNOBACKI,
	SrbDistricts.BRANICEVSKI,
	SrbDistricts.JABLANICKI,
	SrbDistricts.NISAVSKI,
	SrbDistricts.KOLUBARSKI,
	SrbDistricts.BEOGRADSKI,
	SrbDistricts.BORSKI,
	SrbDistricts.NISAVSKI,
	SrbDistricts.ZLATIBORSKI,
	SrbDistricts.SREDNJEBANATSKI,
	SrbDistricts.BEOGRADSKI,
	SrbDistricts.SREDNJEBANATSKI,
	SrbDistricts.SEVERNOBANATSKI,
	SrbDistricts.RASKI,
	SrbDistricts.JUZNOBACKI,
	SrbDistricts.BEOGRADSKI,
	SrbDistricts.JUZNOBANATSKI,
	SrbDistricts.ZAPADNOBACKI,
	SrbDistricts.BEOGRADSKI,
	SrbDistricts.JUZNOBANATSKI,
	SrbDistricts.POMORAVSKI,
	SrbDistricts.BRANICEVSKI,
	SrbDistricts.SREMSKI,
	SrbDistricts.PIROTSKI,
	SrbDistricts.JUZNOBANATSKI,
	SrbDistricts.BRANICEVSKI,
	SrbDistricts.ZLATIBORSKI,
	SrbDistricts.PCINJSKI,
	SrbDistricts.ZLATIBORSKI,
	SrbDistricts.ZLATIBORSKI,
	SrbDistricts.TOPLICKI,
	SrbDistricts.BEOGRADSKI,
	SrbDistricts.SUMADIJSKI,
	SrbDistricts.RASKI,
	SrbDistricts.BEOGRADSKI,
	SrbDistricts.POMORAVSKI,
	SrbDistricts.SEVERNOBANATSKI,
	SrbDistricts.SREDNJEBANATSKI,
	SrbDistricts.PODUNAVSKI,
	SrbDistricts.PODUNAVSKI,
	SrbDistricts.ZAJECARSKI,
	SrbDistricts.ZAPADNOBACKI,
	SrbDistricts.JUZNOBACKI,
	SrbDistricts.SREMSKI,
	SrbDistricts.JUZNOBACKI,
	SrbDistricts.SREMSKI,
	SrbDistricts.BEOGRADSKI,
	SrbDistricts.SEVERNOBACKI,
	SrbDistricts.BEOGRADSKI,
	SrbDistricts.JUZNOBACKI,
	SrbDistricts.JUZNOBACKI,
	SrbDistricts.SUMADIJSKI,
	SrbDistricts.PCINJSKI,
	SrbDistricts.RASINSKI,
	SrbDistricts.RASKI,
	SrbDistricts.POMORAVSKI,
	SrbDistricts.ZLATIBORSKI,
	SrbDistricts.ZLATIBORSKI,
	SrbDistricts.MORAVICKI,
	SrbDistricts.SEVERNOBANATSKI,
	SrbDistricts.MACVANSKI,
	SrbDistricts.SREMSKI
]