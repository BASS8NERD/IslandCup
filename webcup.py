import io

import pandas as pd
import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="CUP OF THE ISLANDS",
    page_icon="🌊",
    layout="wide",
)

GITHUB_RAW_BASE = "https://raw.githubusercontent.com/BASS8NERD/IslandCup/main"

POINTS_BY_IMAGE = {
    1: 2,
    2: 2,
    3: 3,
    4: 9,
    5: 3,
    6: 4,
    7: 6,
    8: 2,
    9: 3,
    10: 3,
    11: 6,
    12: 4,
    13: 4,
    14: 4,
    15: 4,
    16: 4,
    17: 6,
    18: 9,
    19: 6,
    20: 5,
    21: 7,
    22: 9,
    23: 4,
    24: 6,
    25: 6,
    26: 8,
    27: 9,
    28: 2,
    29: 8,
    30: 6,
    31: 4,
    32: 6,
    33: 6,
    34: 7,
    35: 9,
    36: 5,
    37: 5,
    38: 4,
    39: 3,
    40: 7,
}

MARINE_CREATURES = [
    {"Creatura": "ALGA WAKAME", "Foto": f"{GITHUB_RAW_BASE}/1.png", "Valore": 2},
    {"Creatura": "VITE DI MARE", "Foto": f"{GITHUB_RAW_BASE}/2.png", "Valore": 2},
    {"Creatura": "CETRIOLO DI MARE", "Foto": f"{GITHUB_RAW_BASE}/3.png", "Valore": 3},
    {"Creatura": "PORCELLINO DI MARE", "Foto": f"{GITHUB_RAW_BASE}/4.png", "Valore": 9},
    {"Creatura": "STELLA MARINA", "Foto": f"{GITHUB_RAW_BASE}/5.png", "Valore": 3},
    {"Creatura": "RICCIO DI MARE", "Foto": f"{GITHUB_RAW_BASE}/6.png", "Valore": 4},
    {"Creatura": "RICCIO MATITA", "Foto": f"{GITHUB_RAW_BASE}/7.png", "Valore": 6},
    {"Creatura": "ANEMONE DI MARE", "Foto": f"{GITHUB_RAW_BASE}/8.png", "Valore": 2},
    {"Creatura": "MEDUSA AURELIA", "Foto": f"{GITHUB_RAW_BASE}/9.png", "Valore": 3},
    {"Creatura": "NUDIBRANCHI", "Foto": f"{GITHUB_RAW_BASE}/10.png", "Valore": 3},
    {"Creatura": "OSTRICA PINCTADA", "Foto": f"{GITHUB_RAW_BASE}/11.png", "Valore": 6},
    {"Creatura": "COZZA", "Foto": f"{GITHUB_RAW_BASE}/12.png", "Valore": 4},
    {"Creatura": "OSTRICA", "Foto": f"{GITHUB_RAW_BASE}/13.png", "Valore": 4},
    {"Creatura": "CAPASANTA", "Foto": f"{GITHUB_RAW_BASE}/14.png", "Valore": 4},
    {"Creatura": "BUCCINO", "Foto": f"{GITHUB_RAW_BASE}/15.png", "Valore": 4},
    {"Creatura": "LUMACA TURBANTE", "Foto": f"{GITHUB_RAW_BASE}/16.png", "Valore": 4},
    {"Creatura": "ABALONE", "Foto": f"{GITHUB_RAW_BASE}/17.png", "Valore": 6},
    {"Creatura": "TRIDACNA GIGANTE", "Foto": f"{GITHUB_RAW_BASE}/18.png", "Valore": 9},
    {"Creatura": "NAUTILUS", "Foto": f"{GITHUB_RAW_BASE}/19.png", "Valore": 6},
    {"Creatura": "POLPO", "Foto": f"{GITHUB_RAW_BASE}/20.png", "Valore": 5},
    {"Creatura": "POLPO OMBRELLO", "Foto": f"{GITHUB_RAW_BASE}/21.png", "Valore": 7},
    {"Creatura": "CALAMARO VAMPIRO", "Foto": f"{GITHUB_RAW_BASE}/22.png", "Valore": 9},
    {"Creatura": "CALAMARO LUCCIOLA", "Foto": f"{GITHUB_RAW_BASE}/23.png", "Valore": 4},
    {"Creatura": "GRANCHIO GAZAMI", "Foto": f"{GITHUB_RAW_BASE}/24.png", "Valore": 6},
    {"Creatura": "GRANCIPORRO", "Foto": f"{GITHUB_RAW_BASE}/25.png", "Valore": 6},
    {"Creatura": "GRANCHIO DELLA NEVE", "Foto": f"{GITHUB_RAW_BASE}/26.png", "Valore": 8},
    {"Creatura": "GRANCHIO GIGANTE", "Foto": f"{GITHUB_RAW_BASE}/27.png", "Valore": 9},
    {"Creatura": "DENTE DI CANE", "Foto": f"{GITHUB_RAW_BASE}/28.png", "Valore": 2},
    {"Creatura": "GRANCHIO GIG. DEL GIAPPONE", "Foto": f"{GITHUB_RAW_BASE}/29.png", "Valore": 8},
    {"Creatura": "GAMBERO BLACK TIGER", "Foto": f"{GITHUB_RAW_BASE}/30.png", "Valore": 6},
    {"Creatura": "GAMBERETTO BOREALE", "Foto": f"{GITHUB_RAW_BASE}/31.png", "Valore": 4},
    {"Creatura": "GAMBERO MANTIDE", "Foto": f"{GITHUB_RAW_BASE}/32.png", "Valore": 6},
    {"Creatura": "ARAGOSTA MEDITERRANEA", "Foto": f"{GITHUB_RAW_BASE}/33.png", "Valore": 6},
    {"Creatura": "ASTICE", "Foto": f"{GITHUB_RAW_BASE}/34.png", "Valore": 7},
    {"Creatura": "ISOPODE GIGANTE", "Foto": f"{GITHUB_RAW_BASE}/35.png", "Valore": 9},
    {"Creatura": "GRANCHIO FERRO DI CAVALLO", "Foto": f"{GITHUB_RAW_BASE}/36.png", "Valore": 5},
    {"Creatura": "ANANAS DI MARE", "Foto": f"{GITHUB_RAW_BASE}/37.png", "Valore": 5},
    {"Creatura": "ANGUILLA DI GIARDINO", "Foto": f"{GITHUB_RAW_BASE}/38.png", "Valore": 4},
    {"Creatura": "VERME PIATTO", "Foto": f"{GITHUB_RAW_BASE}/39.png", "Valore": 3},
    {"Creatura": "CESTELLO DI VENERE", "Foto": f"{GITHUB_RAW_BASE}/40.png", "Valore": 7},
]

FISHING_CREATURES = [
    {"Creatura": "RODEO", "Foto": f"{GITHUB_RAW_BASE}/41.png", "Valore": 2},
    {"Creatura": "ZACCO", "Foto": f"{GITHUB_RAW_BASE}/42.png", "Valore": 2},
    {"Creatura": "CARASSIO", "Foto": f"{GITHUB_RAW_BASE}/43.png", "Valore": 3},
    {"Creatura": "LASCA", "Foto": f"{GITHUB_RAW_BASE}/44.png", "Valore": 4},
    {"Creatura": "CARPA", "Foto": f"{GITHUB_RAW_BASE}/45.png", "Valore": 5},
    {"Creatura": "KOI", "Foto": f"{GITHUB_RAW_BASE}/46.png", "Valore": 5},
    {"Creatura": "PESCE ROSSO", "Foto": f"{GITHUB_RAW_BASE}/47.png", "Valore": 2},
    {"Creatura": "PESCE TELESCOPIO", "Foto": f"{GITHUB_RAW_BASE}/48.png", "Valore": 3},
    {"Creatura": "RANCHU", "Foto": f"{GITHUB_RAW_BASE}/49.png", "Valore": 4},
    {"Creatura": "KILLIFISH", "Foto": f"{GITHUB_RAW_BASE}/50.png", "Valore": 3},
    {"Creatura": "GAMBERO", "Foto": f"{GITHUB_RAW_BASE}/51.png", "Valore": 3},
    {"Creatura": "APALONE FEROX", "Foto": f"{GITHUB_RAW_BASE}/52.png", "Valore": 5},
    {"Creatura": "TARTARUGA AZZANNATRICE", "Foto": f"{GITHUB_RAW_BASE}/53.png", "Valore": 5},
    {"Creatura": "GIRINO", "Foto": f"{GITHUB_RAW_BASE}/54.png", "Valore": 2},
    {"Creatura": "RANA", "Foto": f"{GITHUB_RAW_BASE}/55.png", "Valore": 3},
    {"Creatura": "GHIOZZO", "Foto": f"{GITHUB_RAW_BASE}/56.png", "Valore": 3},
    {"Creatura": "COBITE", "Foto": f"{GITHUB_RAW_BASE}/57.png", "Valore": 3},
    {"Creatura": "PESCE GATTO", "Foto": f"{GITHUB_RAW_BASE}/58.png", "Valore": 5},
    {"Creatura": "PESCE SERPENTE", "Foto": f"{GITHUB_RAW_BASE}/59.png", "Valore": 6},
    {"Creatura": "PESCE PERSICO", "Foto": f"{GITHUB_RAW_BASE}/60.png", "Valore": 3},
    {"Creatura": "PERCA DORATA", "Foto": f"{GITHUB_RAW_BASE}/61.png", "Valore": 4},
    {"Creatura": "BOCCALONE", "Foto": f"{GITHUB_RAW_BASE}/62.png", "Valore": 5},
    {"Creatura": "TILAPIA", "Foto": f"{GITHUB_RAW_BASE}/63.png", "Valore": 4},
    {"Creatura": "LUCCIO NORDICO", "Foto": f"{GITHUB_RAW_BASE}/64.png", "Valore": 7},
    {"Creatura": "PINGO", "Foto": f"{GITHUB_RAW_BASE}/65.png", "Valore": 3},
    {"Creatura": "AYU", "Foto": f"{GITHUB_RAW_BASE}/66.png", "Valore": 4},
    {"Creatura": "SALMONE GIAPPONESE", "Foto": f"{GITHUB_RAW_BASE}/67.png", "Valore": 5},
    {"Creatura": "SALMERINO ALPINO", "Foto": f"{GITHUB_RAW_BASE}/68.png", "Valore": 6},
    {"Creatura": "TROTA DORATA", "Foto": f"{GITHUB_RAW_BASE}/69.png", "Valore": 6},
    {"Creatura": "TAIMEN", "Foto": f"{GITHUB_RAW_BASE}/70.png", "Valore": 8},
    {"Creatura": "SALMONE", "Foto": f"{GITHUB_RAW_BASE}/71.png", "Valore": 5},
    {"Creatura": "SALMONE REALE", "Foto": f"{GITHUB_RAW_BASE}/72.png", "Valore": 7},
    {"Creatura": "GRANCHIO GUANTATO", "Foto": f"{GITHUB_RAW_BASE}/73.png", "Valore": 3},
    {"Creatura": "GUPPY", "Foto": f"{GITHUB_RAW_BASE}/74.png", "Valore": 2},
    {"Creatura": "GARRA RUFA", "Foto": f"{GITHUB_RAW_BASE}/75.png", "Valore": 3},
    {"Creatura": "PESCE ANGELO", "Foto": f"{GITHUB_RAW_BASE}/76.png", "Valore": 3},
    {"Creatura": "BETTA", "Foto": f"{GITHUB_RAW_BASE}/77.png", "Valore": 4},
    {"Creatura": "PESCE NEON", "Foto": f"{GITHUB_RAW_BASE}/78.png", "Valore": 2},
    {"Creatura": "PESCE ARCOBALENO", "Foto": f"{GITHUB_RAW_BASE}/79.png", "Valore": 3},
    {"Creatura": "PESCE PIRANHA", "Foto": f"{GITHUB_RAW_BASE}/80.png", "Valore": 4},
    {"Creatura": "AROWANA", "Foto": f"{GITHUB_RAW_BASE}/81.png", "Valore": 6},
    {"Creatura": "DORADO", "Foto": f"{GITHUB_RAW_BASE}/82.png", "Valore": 7},
    {"Creatura": "LUCCIO", "Foto": f"{GITHUB_RAW_BASE}/83.png", "Valore": 7},
    {"Creatura": "PIRARUCU", "Foto": f"{GITHUB_RAW_BASE}/84.png", "Valore": 8},
    {"Creatura": "POLIPTERIDE", "Foto": f"{GITHUB_RAW_BASE}/85.png", "Valore": 6},
    {"Creatura": "STORIONE", "Foto": f"{GITHUB_RAW_BASE}/86.png", "Valore": 9},
    {"Creatura": "CAVOLINIA", "Foto": f"{GITHUB_RAW_BASE}/87.png", "Valore": 2},
    {"Creatura": "IPPOCAMPO", "Foto": f"{GITHUB_RAW_BASE}/88.png", "Valore": 2},
    {"Creatura": "PESCE PAGLIACCIO", "Foto": f"{GITHUB_RAW_BASE}/89.png", "Valore": 2},
    {"Creatura": "PESCE CHIRURGO", "Foto": f"{GITHUB_RAW_BASE}/90.png", "Valore": 4},
    {"Creatura": "PESCE FARFALLA", "Foto": f"{GITHUB_RAW_BASE}/91.png", "Valore": 3},
    {"Creatura": "PESCE NAPOLEONE", "Foto": f"{GITHUB_RAW_BASE}/92.png", "Valore": 9},
    {"Creatura": "LEONE ZEBRATO", "Foto": f"{GITHUB_RAW_BASE}/93.png", "Valore": 4},
    {"Creatura": "PESCE PALLA", "Foto": f"{GITHUB_RAW_BASE}/94.png", "Valore": 4},
    {"Creatura": "PESCE ISTRICE", "Foto": f"{GITHUB_RAW_BASE}/95.png", "Valore": 4},
    {"Creatura": "ACCIUGA", "Foto": f"{GITHUB_RAW_BASE}/96.png", "Valore": 4},
    {"Creatura": "SGOMBRO", "Foto": f"{GITHUB_RAW_BASE}/97.png", "Valore": 3},
    {"Creatura": "ISHIDAI", "Foto": f"{GITHUB_RAW_BASE}/98.png", "Valore": 5},
    {"Creatura": "SPIGOLA", "Foto": f"{GITHUB_RAW_BASE}/99.png", "Valore": 6},
    {"Creatura": "LUTIANO ROSSO", "Foto": f"{GITHUB_RAW_BASE}/100.png", "Valore": 5},
    {"Creatura": "PLATESSA", "Foto": f"{GITHUB_RAW_BASE}/101.png", "Valore": 4},
    {"Creatura": "SOGLIOLA", "Foto": f"{GITHUB_RAW_BASE}/102.png", "Valore": 6},
    {"Creatura": "CALAMARO", "Foto": f"{GITHUB_RAW_BASE}/103.png", "Valore": 4},
    {"Creatura": "MURENA", "Foto": f"{GITHUB_RAW_BASE}/104.png", "Valore": 1},
    {"Creatura": "MURENA A NASTRO", "Foto": f"{GITHUB_RAW_BASE}/105.png", "Valore": 1},
    {"Creatura": "TONNO", "Foto": f"{GITHUB_RAW_BASE}/106.png", "Valore": 9},
    {"Creatura": "MARLIN BLU", "Foto": f"{GITHUB_RAW_BASE}/107.png", "Valore": 9},
    {"Creatura": "CARANGO GIGANTE", "Foto": f"{GITHUB_RAW_BASE}/108.png", "Valore": 8},
    {"Creatura": "LAMPUGA", "Foto": f"{GITHUB_RAW_BASE}/109.png", "Valore": 8},
    {"Creatura": "PESCE LUNA", "Foto": f"{GITHUB_RAW_BASE}/110.png", "Valore": 9},
    {"Creatura": "RAZZA", "Foto": f"{GITHUB_RAW_BASE}/111.png", "Valore": 7},
    {"Creatura": "SQUALO SEGA", "Foto": f"{GITHUB_RAW_BASE}/112.png", "Valore": 9},
    {"Creatura": "PESCE MARTELLO", "Foto": f"{GITHUB_RAW_BASE}/113.png", "Valore": 9},
    {"Creatura": "SQUALO BIANCO", "Foto": f"{GITHUB_RAW_BASE}/114.png", "Valore": 8},
    {"Creatura": "SQUALO BALENA", "Foto": f"{GITHUB_RAW_BASE}/115.png", "Valore": 9},
    {"Creatura": "REMORA", "Foto": f"{GITHUB_RAW_BASE}/116.png", "Valore": 6},
    {"Creatura": "PESCE ABISSALE", "Foto": f"{GITHUB_RAW_BASE}/117.png", "Valore": 5},
    {"Creatura": "PESCE REMO", "Foto": f"{GITHUB_RAW_BASE}/118.png", "Valore": 9},
    {"Creatura": "MACROPINNA", "Foto": f"{GITHUB_RAW_BASE}/119.png", "Valore": 5},
    {"Creatura": "CELACANTO", "Foto": f"{GITHUB_RAW_BASE}/120.png", "Valore": 9},
]

INSECT_CREATURES = [
    {"Creatura": "Insetto 1", "Foto": f"{GITHUB_RAW_BASE}/121.png", "Valore": 10},
    {"Creatura": "Insetto 2", "Foto": f"{GITHUB_RAW_BASE}/122.png", "Valore": 10},
    {"Creatura": "Insetto 3", "Foto": f"{GITHUB_RAW_BASE}/123.png", "Valore": 10},
    {"Creatura": "Insetto 4", "Foto": f"{GITHUB_RAW_BASE}/124.png", "Valore": 10},
    {"Creatura": "Insetto 5", "Foto": f"{GITHUB_RAW_BASE}/125.png", "Valore": 10},
    {"Creatura": "Insetto 6", "Foto": f"{GITHUB_RAW_BASE}/126.png", "Valore": 10},
    {"Creatura": "Insetto 7", "Foto": f"{GITHUB_RAW_BASE}/127.png", "Valore": 10},
    {"Creatura": "Insetto 8", "Foto": f"{GITHUB_RAW_BASE}/128.png", "Valore": 10},
    {"Creatura": "Insetto 9", "Foto": f"{GITHUB_RAW_BASE}/129.png", "Valore": 10},
    {"Creatura": "Insetto 10", "Foto": f"{GITHUB_RAW_BASE}/130.png", "Valore": 10},
    {"Creatura": "Insetto 11", "Foto": f"{GITHUB_RAW_BASE}/131.png", "Valore": 10},
    {"Creatura": "Insetto 12", "Foto": f"{GITHUB_RAW_BASE}/132.png", "Valore": 10},
    {"Creatura": "Insetto 13", "Foto": f"{GITHUB_RAW_BASE}/133.png", "Valore": 10},
    {"Creatura": "Insetto 14", "Foto": f"{GITHUB_RAW_BASE}/134.png", "Valore": 10},
    {"Creatura": "Insetto 15", "Foto": f"{GITHUB_RAW_BASE}/135.png", "Valore": 10},
    {"Creatura": "Insetto 16", "Foto": f"{GITHUB_RAW_BASE}/136.png", "Valore": 10},
    {"Creatura": "Insetto 17", "Foto": f"{GITHUB_RAW_BASE}/137.png", "Valore": 10},
    {"Creatura": "Insetto 18", "Foto": f"{GITHUB_RAW_BASE}/138.png", "Valore": 10},
    {"Creatura": "Insetto 19", "Foto": f"{GITHUB_RAW_BASE}/139.png", "Valore": 10},
    {"Creatura": "Insetto 20", "Foto": f"{GITHUB_RAW_BASE}/140.png", "Valore": 10},
    {"Creatura": "Insetto 21", "Foto": f"{GITHUB_RAW_BASE}/141.png", "Valore": 10},
    {"Creatura": "Insetto 22", "Foto": f"{GITHUB_RAW_BASE}/142.png", "Valore": 10},
    {"Creatura": "Insetto 23", "Foto": f"{GITHUB_RAW_BASE}/143.png", "Valore": 10},
    {"Creatura": "Insetto 24", "Foto": f"{GITHUB_RAW_BASE}/144.png", "Valore": 10},
    {"Creatura": "Insetto 25", "Foto": f"{GITHUB_RAW_BASE}/145.png", "Valore": 10},
    {"Creatura": "Insetto 26", "Foto": f"{GITHUB_RAW_BASE}/146.png", "Valore": 10},
    {"Creatura": "Insetto 27", "Foto": f"{GITHUB_RAW_BASE}/147.png", "Valore": 10},
    {"Creatura": "Insetto 28", "Foto": f"{GITHUB_RAW_BASE}/148.png", "Valore": 10},
    {"Creatura": "Insetto 29", "Foto": f"{GITHUB_RAW_BASE}/149.png", "Valore": 10},
    {"Creatura": "Insetto 30", "Foto": f"{GITHUB_RAW_BASE}/150.png", "Valore": 10},
    {"Creatura": "Insetto 31", "Foto": f"{GITHUB_RAW_BASE}/151.png", "Valore": 10},
    {"Creatura": "Insetto 32", "Foto": f"{GITHUB_RAW_BASE}/152.png", "Valore": 10},
    {"Creatura": "Insetto 33", "Foto": f"{GITHUB_RAW_BASE}/153.png", "Valore": 10},
    {"Creatura": "Insetto 34", "Foto": f"{GITHUB_RAW_BASE}/154.png", "Valore": 10},
    {"Creatura": "Insetto 35", "Foto": f"{GITHUB_RAW_BASE}/155.png", "Valore": 10},
    {"Creatura": "Insetto 36", "Foto": f"{GITHUB_RAW_BASE}/156.png", "Valore": 10},
    {"Creatura": "Insetto 37", "Foto": f"{GITHUB_RAW_BASE}/157.png", "Valore": 10},
    {"Creatura": "Insetto 38", "Foto": f"{GITHUB_RAW_BASE}/158.png", "Valore": 10},
    {"Creatura": "Insetto 39", "Foto": f"{GITHUB_RAW_BASE}/159.png", "Valore": 10},
    {"Creatura": "Insetto 40", "Foto": f"{GITHUB_RAW_BASE}/160.png", "Valore": 10},
    {"Creatura": "Insetto 41", "Foto": f"{GITHUB_RAW_BASE}/161.png", "Valore": 10},
    {"Creatura": "Insetto 42", "Foto": f"{GITHUB_RAW_BASE}/162.png", "Valore": 10},
    {"Creatura": "Insetto 43", "Foto": f"{GITHUB_RAW_BASE}/163.png", "Valore": 10},
    {"Creatura": "Insetto 44", "Foto": f"{GITHUB_RAW_BASE}/164.png", "Valore": 10},
    {"Creatura": "Insetto 45", "Foto": f"{GITHUB_RAW_BASE}/165.png", "Valore": 10},
    {"Creatura": "Insetto 46", "Foto": f"{GITHUB_RAW_BASE}/166.png", "Valore": 10},
    {"Creatura": "Insetto 47", "Foto": f"{GITHUB_RAW_BASE}/167.png", "Valore": 10},
    {"Creatura": "Insetto 48", "Foto": f"{GITHUB_RAW_BASE}/168.png", "Valore": 10},
    {"Creatura": "Insetto 49", "Foto": f"{GITHUB_RAW_BASE}/169.png", "Valore": 10},
    {"Creatura": "Insetto 50", "Foto": f"{GITHUB_RAW_BASE}/170.png", "Valore": 10},
    {"Creatura": "Insetto 51", "Foto": f"{GITHUB_RAW_BASE}/171.png", "Valore": 10},
    {"Creatura": "Insetto 52", "Foto": f"{GITHUB_RAW_BASE}/172.png", "Valore": 10},
    {"Creatura": "Insetto 53", "Foto": f"{GITHUB_RAW_BASE}/173.png", "Valore": 10},
    {"Creatura": "Insetto 54", "Foto": f"{GITHUB_RAW_BASE}/174.png", "Valore": 10},
    {"Creatura": "Insetto 55", "Foto": f"{GITHUB_RAW_BASE}/175.png", "Valore": 10},
    {"Creatura": "Insetto 56", "Foto": f"{GITHUB_RAW_BASE}/176.png", "Valore": 10},
    {"Creatura": "Insetto 57", "Foto": f"{GITHUB_RAW_BASE}/177.png", "Valore": 10},
    {"Creatura": "Insetto 58", "Foto": f"{GITHUB_RAW_BASE}/178.png", "Valore": 10},
    {"Creatura": "Insetto 59", "Foto": f"{GITHUB_RAW_BASE}/179.png", "Valore": 10},
    {"Creatura": "Insetto 60", "Foto": f"{GITHUB_RAW_BASE}/180.png", "Valore": 10},
    {"Creatura": "Insetto 61", "Foto": f"{GITHUB_RAW_BASE}/181.png", "Valore": 10},
    {"Creatura": "Insetto 62", "Foto": f"{GITHUB_RAW_BASE}/182.png", "Valore": 10},
    {"Creatura": "Insetto 63", "Foto": f"{GITHUB_RAW_BASE}/183.png", "Valore": 10},
    {"Creatura": "Insetto 64", "Foto": f"{GITHUB_RAW_BASE}/184.png", "Valore": 10},
    {"Creatura": "Insetto 65", "Foto": f"{GITHUB_RAW_BASE}/185.png", "Valore": 10},
    {"Creatura": "Insetto 66", "Foto": f"{GITHUB_RAW_BASE}/186.png", "Valore": 10},
    {"Creatura": "Insetto 67", "Foto": f"{GITHUB_RAW_BASE}/187.png", "Valore": 10},
    {"Creatura": "Insetto 68", "Foto": f"{GITHUB_RAW_BASE}/188.png", "Valore": 10},
    {"Creatura": "Insetto 69", "Foto": f"{GITHUB_RAW_BASE}/189.png", "Valore": 10},
    {"Creatura": "Insetto 70", "Foto": f"{GITHUB_RAW_BASE}/190.png", "Valore": 10},
    {"Creatura": "Insetto 71", "Foto": f"{GITHUB_RAW_BASE}/191.png", "Valore": 10},
    {"Creatura": "Insetto 72", "Foto": f"{GITHUB_RAW_BASE}/192.png", "Valore": 10},
    {"Creatura": "Insetto 73", "Foto": f"{GITHUB_RAW_BASE}/193.png", "Valore": 10},
    {"Creatura": "Insetto 74", "Foto": f"{GITHUB_RAW_BASE}/194.png", "Valore": 10},
    {"Creatura": "Insetto 75", "Foto": f"{GITHUB_RAW_BASE}/195.png", "Valore": 10},
    {"Creatura": "Insetto 76", "Foto": f"{GITHUB_RAW_BASE}/196.png", "Valore": 10},
    {"Creatura": "Insetto 77", "Foto": f"{GITHUB_RAW_BASE}/197.png", "Valore": 10},
    {"Creatura": "Insetto 78", "Foto": f"{GITHUB_RAW_BASE}/198.png", "Valore": 10},
    {"Creatura": "Insetto 79", "Foto": f"{GITHUB_RAW_BASE}/199.png", "Valore": 10},
    {"Creatura": "Insetto 80", "Foto": f"{GITHUB_RAW_BASE}/200.png", "Valore": 10},
]

MIX_CREATURES = [
    {"Creatura": "Mix 1", "Foto": f"{GITHUB_RAW_BASE}/201.png", "Valore": 10},
    {"Creatura": "Mix 2", "Foto": f"{GITHUB_RAW_BASE}/202.png", "Valore": 10},
    {"Creatura": "Mix 3", "Foto": f"{GITHUB_RAW_BASE}/203.png", "Valore": 10},
    {"Creatura": "Mix 4", "Foto": f"{GITHUB_RAW_BASE}/204.png", "Valore": 10},
    {"Creatura": "Mix 5", "Foto": f"{GITHUB_RAW_BASE}/205.png", "Valore": 10},
    {"Creatura": "Mix 6", "Foto": f"{GITHUB_RAW_BASE}/206.png", "Valore": 10},
    {"Creatura": "Mix 7", "Foto": f"{GITHUB_RAW_BASE}/207.png", "Valore": 10},
    {"Creatura": "Mix 8", "Foto": f"{GITHUB_RAW_BASE}/208.png", "Valore": 10},
    {"Creatura": "Mix 9", "Foto": f"{GITHUB_RAW_BASE}/209.png", "Valore": 10},
    {"Creatura": "Mix 10", "Foto": f"{GITHUB_RAW_BASE}/210.png", "Valore": 10},
    {"Creatura": "Mix 11", "Foto": f"{GITHUB_RAW_BASE}/211.png", "Valore": 10},
    {"Creatura": "Mix 12", "Foto": f"{GITHUB_RAW_BASE}/212.png", "Valore": 10},
    {"Creatura": "Mix 13", "Foto": f"{GITHUB_RAW_BASE}/213.png", "Valore": 10},
    {"Creatura": "Mix 14", "Foto": f"{GITHUB_RAW_BASE}/214.png", "Valore": 10},
    {"Creatura": "Mix 15", "Foto": f"{GITHUB_RAW_BASE}/215.png", "Valore": 10},
    {"Creatura": "Mix 16", "Foto": f"{GITHUB_RAW_BASE}/216.png", "Valore": 10},
    {"Creatura": "Mix 17", "Foto": f"{GITHUB_RAW_BASE}/217.png", "Valore": 10},
    {"Creatura": "Mix 18", "Foto": f"{GITHUB_RAW_BASE}/218.png", "Valore": 10},
    {"Creatura": "Mix 19", "Foto": f"{GITHUB_RAW_BASE}/219.png", "Valore": 10},
    {"Creatura": "Mix 20", "Foto": f"{GITHUB_RAW_BASE}/220.png", "Valore": 10},
    {"Creatura": "Mix 21", "Foto": f"{GITHUB_RAW_BASE}/221.png", "Valore": 10},
    {"Creatura": "Mix 22", "Foto": f"{GITHUB_RAW_BASE}/222.png", "Valore": 10},
    {"Creatura": "Mix 23", "Foto": f"{GITHUB_RAW_BASE}/223.png", "Valore": 10},
    {"Creatura": "Mix 24", "Foto": f"{GITHUB_RAW_BASE}/224.png", "Valore": 10},
    {"Creatura": "Mix 25", "Foto": f"{GITHUB_RAW_BASE}/225.png", "Valore": 10},
    {"Creatura": "Mix 26", "Foto": f"{GITHUB_RAW_BASE}/226.png", "Valore": 10},
    {"Creatura": "Mix 27", "Foto": f"{GITHUB_RAW_BASE}/227.png", "Valore": 10},
    {"Creatura": "Mix 28", "Foto": f"{GITHUB_RAW_BASE}/228.png", "Valore": 10},
    {"Creatura": "Mix 29", "Foto": f"{GITHUB_RAW_BASE}/229.png", "Valore": 10},
    {"Creatura": "Mix 30", "Foto": f"{GITHUB_RAW_BASE}/230.png", "Valore": 10},
    {"Creatura": "Mix 31", "Foto": f"{GITHUB_RAW_BASE}/231.png", "Valore": 10},
    {"Creatura": "Mix 32", "Foto": f"{GITHUB_RAW_BASE}/232.png", "Valore": 10},
    {"Creatura": "Mix 33", "Foto": f"{GITHUB_RAW_BASE}/233.png", "Valore": 10},
    {"Creatura": "Mix 34", "Foto": f"{GITHUB_RAW_BASE}/234.png", "Valore": 10},
    {"Creatura": "Mix 35", "Foto": f"{GITHUB_RAW_BASE}/235.png", "Valore": 10},
    {"Creatura": "Mix 36", "Foto": f"{GITHUB_RAW_BASE}/236.png", "Valore": 10},
    {"Creatura": "Mix 37", "Foto": f"{GITHUB_RAW_BASE}/237.png", "Valore": 10},
    {"Creatura": "Mix 38", "Foto": f"{GITHUB_RAW_BASE}/238.png", "Valore": 10},
    {"Creatura": "Mix 39", "Foto": f"{GITHUB_RAW_BASE}/239.png", "Valore": 10},
    {"Creatura": "Mix 40", "Foto": f"{GITHUB_RAW_BASE}/240.png", "Valore": 10},
    {"Creatura": "Mix 41", "Foto": f"{GITHUB_RAW_BASE}/241.png", "Valore": 10},
    {"Creatura": "Mix 42", "Foto": f"{GITHUB_RAW_BASE}/242.png", "Valore": 10},
    {"Creatura": "Mix 43", "Foto": f"{GITHUB_RAW_BASE}/243.png", "Valore": 10},
    {"Creatura": "Mix 44", "Foto": f"{GITHUB_RAW_BASE}/244.png", "Valore": 10},
    {"Creatura": "Mix 45", "Foto": f"{GITHUB_RAW_BASE}/245.png", "Valore": 10},
    {"Creatura": "Mix 46", "Foto": f"{GITHUB_RAW_BASE}/246.png", "Valore": 10},
    {"Creatura": "Mix 47", "Foto": f"{GITHUB_RAW_BASE}/247.png", "Valore": 10},
    {"Creatura": "Mix 48", "Foto": f"{GITHUB_RAW_BASE}/248.png", "Valore": 10},
    {"Creatura": "Mix 49", "Foto": f"{GITHUB_RAW_BASE}/249.png", "Valore": 10},
    {"Creatura": "Mix 50", "Foto": f"{GITHUB_RAW_BASE}/250.png", "Valore": 10},
    {"Creatura": "Mix 51", "Foto": f"{GITHUB_RAW_BASE}/251.png", "Valore": 10},
    {"Creatura": "Mix 52", "Foto": f"{GITHUB_RAW_BASE}/252.png", "Valore": 10},
    {"Creatura": "Mix 53", "Foto": f"{GITHUB_RAW_BASE}/253.png", "Valore": 10},
    {"Creatura": "Mix 54", "Foto": f"{GITHUB_RAW_BASE}/254.png", "Valore": 10},
    {"Creatura": "Mix 55", "Foto": f"{GITHUB_RAW_BASE}/255.png", "Valore": 10},
    {"Creatura": "Mix 56", "Foto": f"{GITHUB_RAW_BASE}/256.png", "Valore": 10},
    {"Creatura": "Mix 57", "Foto": f"{GITHUB_RAW_BASE}/257.png", "Valore": 10},
    {"Creatura": "Mix 58", "Foto": f"{GITHUB_RAW_BASE}/258.png", "Valore": 10},
    {"Creatura": "Mix 59", "Foto": f"{GITHUB_RAW_BASE}/259.png", "Valore": 10},
    {"Creatura": "Mix 60", "Foto": f"{GITHUB_RAW_BASE}/260.png", "Valore": 10},
    {"Creatura": "Mix 61", "Foto": f"{GITHUB_RAW_BASE}/261.png", "Valore": 10},
    {"Creatura": "Mix 62", "Foto": f"{GITHUB_RAW_BASE}/262.png", "Valore": 10},
    {"Creatura": "Mix 63", "Foto": f"{GITHUB_RAW_BASE}/263.png", "Valore": 10},
    {"Creatura": "Mix 64", "Foto": f"{GITHUB_RAW_BASE}/264.png", "Valore": 10},
    {"Creatura": "Mix 65", "Foto": f"{GITHUB_RAW_BASE}/265.png", "Valore": 10},
    {"Creatura": "Mix 66", "Foto": f"{GITHUB_RAW_BASE}/266.png", "Valore": 10},
    {"Creatura": "Mix 67", "Foto": f"{GITHUB_RAW_BASE}/267.png", "Valore": 10},
    {"Creatura": "Mix 68", "Foto": f"{GITHUB_RAW_BASE}/268.png", "Valore": 10},
    {"Creatura": "Mix 69", "Foto": f"{GITHUB_RAW_BASE}/269.png", "Valore": 10},
    {"Creatura": "Mix 70", "Foto": f"{GITHUB_RAW_BASE}/270.png", "Valore": 10},
    {"Creatura": "Mix 71", "Foto": f"{GITHUB_RAW_BASE}/271.png", "Valore": 10},
    {"Creatura": "Mix 72", "Foto": f"{GITHUB_RAW_BASE}/272.png", "Valore": 10},
    {"Creatura": "Mix 73", "Foto": f"{GITHUB_RAW_BASE}/273.png", "Valore": 10},
    {"Creatura": "Mix 74", "Foto": f"{GITHUB_RAW_BASE}/274.png", "Valore": 10},
    {"Creatura": "Mix 75", "Foto": f"{GITHUB_RAW_BASE}/275.png", "Valore": 10},
    {"Creatura": "Mix 76", "Foto": f"{GITHUB_RAW_BASE}/276.png", "Valore": 10},
    {"Creatura": "Mix 77", "Foto": f"{GITHUB_RAW_BASE}/277.png", "Valore": 10},
    {"Creatura": "Mix 78", "Foto": f"{GITHUB_RAW_BASE}/278.png", "Valore": 10},
    {"Creatura": "Mix 79", "Foto": f"{GITHUB_RAW_BASE}/279.png", "Valore": 10},
    {"Creatura": "Mix 80", "Foto": f"{GITHUB_RAW_BASE}/280.png", "Valore": 10},
    {"Creatura": "Mix 81", "Foto": f"{GITHUB_RAW_BASE}/281.png", "Valore": 10},
    {"Creatura": "Mix 82", "Foto": f"{GITHUB_RAW_BASE}/282.png", "Valore": 10},
    {"Creatura": "Mix 83", "Foto": f"{GITHUB_RAW_BASE}/283.png", "Valore": 10},
    {"Creatura": "Mix 84", "Foto": f"{GITHUB_RAW_BASE}/284.png", "Valore": 10},
    {"Creatura": "Mix 85", "Foto": f"{GITHUB_RAW_BASE}/285.png", "Valore": 10},
    {"Creatura": "Mix 86", "Foto": f"{GITHUB_RAW_BASE}/286.png", "Valore": 10},
    {"Creatura": "Mix 87", "Foto": f"{GITHUB_RAW_BASE}/287.png", "Valore": 10},
    {"Creatura": "Mix 88", "Foto": f"{GITHUB_RAW_BASE}/288.png", "Valore": 10},
    {"Creatura": "Mix 89", "Foto": f"{GITHUB_RAW_BASE}/289.png", "Valore": 10},
    {"Creatura": "Mix 90", "Foto": f"{GITHUB_RAW_BASE}/290.png", "Valore": 10},
    {"Creatura": "Mix 91", "Foto": f"{GITHUB_RAW_BASE}/291.png", "Valore": 10},
    {"Creatura": "Mix 92", "Foto": f"{GITHUB_RAW_BASE}/292.png", "Valore": 10},
    {"Creatura": "Mix 93", "Foto": f"{GITHUB_RAW_BASE}/293.png", "Valore": 10},
    {"Creatura": "Mix 94", "Foto": f"{GITHUB_RAW_BASE}/294.png", "Valore": 10},
    {"Creatura": "Mix 95", "Foto": f"{GITHUB_RAW_BASE}/295.png", "Valore": 10},
    {"Creatura": "Mix 96", "Foto": f"{GITHUB_RAW_BASE}/296.png", "Valore": 10},
    {"Creatura": "Mix 97", "Foto": f"{GITHUB_RAW_BASE}/297.png", "Valore": 10},
    {"Creatura": "Mix 98", "Foto": f"{GITHUB_RAW_BASE}/298.png", "Valore": 10},
    {"Creatura": "Mix 99", "Foto": f"{GITHUB_RAW_BASE}/299.png", "Valore": 10},
    {"Creatura": "Mix 100", "Foto": f"{GITHUB_RAW_BASE}/300.png", "Valore": 10},
    {"Creatura": "Mix 101", "Foto": f"{GITHUB_RAW_BASE}/301.png", "Valore": 10},
    {"Creatura": "Mix 102", "Foto": f"{GITHUB_RAW_BASE}/302.png", "Valore": 10},
    {"Creatura": "Mix 103", "Foto": f"{GITHUB_RAW_BASE}/303.png", "Valore": 10},
    {"Creatura": "Mix 104", "Foto": f"{GITHUB_RAW_BASE}/304.png", "Valore": 10},
    {"Creatura": "Mix 105", "Foto": f"{GITHUB_RAW_BASE}/305.png", "Valore": 10},
    {"Creatura": "Mix 106", "Foto": f"{GITHUB_RAW_BASE}/306.png", "Valore": 10},
    {"Creatura": "Mix 107", "Foto": f"{GITHUB_RAW_BASE}/307.png", "Valore": 10},
    {"Creatura": "Mix 108", "Foto": f"{GITHUB_RAW_BASE}/308.png", "Valore": 10},
    {"Creatura": "Mix 109", "Foto": f"{GITHUB_RAW_BASE}/309.png", "Valore": 10},
    {"Creatura": "Mix 110", "Foto": f"{GITHUB_RAW_BASE}/310.png", "Valore": 10},
    {"Creatura": "Mix 111", "Foto": f"{GITHUB_RAW_BASE}/311.png", "Valore": 10},
    {"Creatura": "Mix 112", "Foto": f"{GITHUB_RAW_BASE}/312.png", "Valore": 10},
    {"Creatura": "Mix 113", "Foto": f"{GITHUB_RAW_BASE}/313.png", "Valore": 10},
    {"Creatura": "Mix 114", "Foto": f"{GITHUB_RAW_BASE}/314.png", "Valore": 10},
    {"Creatura": "Mix 115", "Foto": f"{GITHUB_RAW_BASE}/315.png", "Valore": 10},
    {"Creatura": "Mix 116", "Foto": f"{GITHUB_RAW_BASE}/316.png", "Valore": 10},
    {"Creatura": "Mix 117", "Foto": f"{GITHUB_RAW_BASE}/317.png", "Valore": 10},
    {"Creatura": "Mix 118", "Foto": f"{GITHUB_RAW_BASE}/318.png", "Valore": 10},
    {"Creatura": "Mix 119", "Foto": f"{GITHUB_RAW_BASE}/319.png", "Valore": 10},
    {"Creatura": "Mix 120", "Foto": f"{GITHUB_RAW_BASE}/320.png", "Valore": 10},
    {"Creatura": "Mix 121", "Foto": f"{GITHUB_RAW_BASE}/321.png", "Valore": 10},
    {"Creatura": "Mix 122", "Foto": f"{GITHUB_RAW_BASE}/322.png", "Valore": 10},
    {"Creatura": "Mix 123", "Foto": f"{GITHUB_RAW_BASE}/323.png", "Valore": 10},
    {"Creatura": "Mix 124", "Foto": f"{GITHUB_RAW_BASE}/324.png", "Valore": 10},
    {"Creatura": "Mix 125", "Foto": f"{GITHUB_RAW_BASE}/325.png", "Valore": 10},
    {"Creatura": "Mix 126", "Foto": f"{GITHUB_RAW_BASE}/326.png", "Valore": 10},
    {"Creatura": "Mix 127", "Foto": f"{GITHUB_RAW_BASE}/327.png", "Valore": 10},
    {"Creatura": "Mix 128", "Foto": f"{GITHUB_RAW_BASE}/328.png", "Valore": 10},
    {"Creatura": "Mix 129", "Foto": f"{GITHUB_RAW_BASE}/329.png", "Valore": 10},
    {"Creatura": "Mix 130", "Foto": f"{GITHUB_RAW_BASE}/330.png", "Valore": 10},
    {"Creatura": "Mix 131", "Foto": f"{GITHUB_RAW_BASE}/331.png", "Valore": 10},
    {"Creatura": "Mix 132", "Foto": f"{GITHUB_RAW_BASE}/332.png", "Valore": 10},
    {"Creatura": "Mix 133", "Foto": f"{GITHUB_RAW_BASE}/333.png", "Valore": 10},
    {"Creatura": "Mix 134", "Foto": f"{GITHUB_RAW_BASE}/334.png", "Valore": 10},
    {"Creatura": "Mix 135", "Foto": f"{GITHUB_RAW_BASE}/335.png", "Valore": 10},
    {"Creatura": "Mix 136", "Foto": f"{GITHUB_RAW_BASE}/336.png", "Valore": 10},
    {"Creatura": "Mix 137", "Foto": f"{GITHUB_RAW_BASE}/337.png", "Valore": 10},
    {"Creatura": "Mix 138", "Foto": f"{GITHUB_RAW_BASE}/338.png", "Valore": 10},
    {"Creatura": "Mix 139", "Foto": f"{GITHUB_RAW_BASE}/339.png", "Valore": 10},
    {"Creatura": "Mix 140", "Foto": f"{GITHUB_RAW_BASE}/340.png", "Valore": 10},
    {"Creatura": "Mix 141", "Foto": f"{GITHUB_RAW_BASE}/341.png", "Valore": 10},
    {"Creatura": "Mix 142", "Foto": f"{GITHUB_RAW_BASE}/342.png", "Valore": 10},
    {"Creatura": "Mix 143", "Foto": f"{GITHUB_RAW_BASE}/343.png", "Valore": 10},
    {"Creatura": "Mix 144", "Foto": f"{GITHUB_RAW_BASE}/344.png", "Valore": 10},
    {"Creatura": "Mix 145", "Foto": f"{GITHUB_RAW_BASE}/345.png", "Valore": 10},
    {"Creatura": "Mix 146", "Foto": f"{GITHUB_RAW_BASE}/346.png", "Valore": 10},
    {"Creatura": "Mix 147", "Foto": f"{GITHUB_RAW_BASE}/347.png", "Valore": 10},
    {"Creatura": "Mix 148", "Foto": f"{GITHUB_RAW_BASE}/348.png", "Valore": 10},
    {"Creatura": "Mix 149", "Foto": f"{GITHUB_RAW_BASE}/349.png", "Valore": 10},
    {"Creatura": "Mix 150", "Foto": f"{GITHUB_RAW_BASE}/350.png", "Valore": 10},
    {"Creatura": "Mix 151", "Foto": f"{GITHUB_RAW_BASE}/351.png", "Valore": 10},
    {"Creatura": "Mix 152", "Foto": f"{GITHUB_RAW_BASE}/352.png", "Valore": 10},
    {"Creatura": "Mix 153", "Foto": f"{GITHUB_RAW_BASE}/353.png", "Valore": 10},
    {"Creatura": "Mix 154", "Foto": f"{GITHUB_RAW_BASE}/354.png", "Valore": 10},
    {"Creatura": "Mix 155", "Foto": f"{GITHUB_RAW_BASE}/355.png", "Valore": 10},
    {"Creatura": "Mix 156", "Foto": f"{GITHUB_RAW_BASE}/356.png", "Valore": 10},
    {"Creatura": "Mix 157", "Foto": f"{GITHUB_RAW_BASE}/357.png", "Valore": 10},
    {"Creatura": "Mix 158", "Foto": f"{GITHUB_RAW_BASE}/358.png", "Valore": 10},
    {"Creatura": "Mix 159", "Foto": f"{GITHUB_RAW_BASE}/359.png", "Valore": 10},
    {"Creatura": "Mix 160", "Foto": f"{GITHUB_RAW_BASE}/360.png", "Valore": 10},
    {"Creatura": "Mix 161", "Foto": f"{GITHUB_RAW_BASE}/361.png", "Valore": 10},
    {"Creatura": "Mix 162", "Foto": f"{GITHUB_RAW_BASE}/362.png", "Valore": 10},
    {"Creatura": "Mix 163", "Foto": f"{GITHUB_RAW_BASE}/363.png", "Valore": 10},
    {"Creatura": "Mix 164", "Foto": f"{GITHUB_RAW_BASE}/364.png", "Valore": 10},
    {"Creatura": "Mix 165", "Foto": f"{GITHUB_RAW_BASE}/365.png", "Valore": 10},
    {"Creatura": "Mix 166", "Foto": f"{GITHUB_RAW_BASE}/366.png", "Valore": 10},
    {"Creatura": "Mix 167", "Foto": f"{GITHUB_RAW_BASE}/367.png", "Valore": 10},
    {"Creatura": "Mix 168", "Foto": f"{GITHUB_RAW_BASE}/368.png", "Valore": 10},
    {"Creatura": "Mix 169", "Foto": f"{GITHUB_RAW_BASE}/369.png", "Valore": 10},
    {"Creatura": "Mix 170", "Foto": f"{GITHUB_RAW_BASE}/370.png", "Valore": 10},
    {"Creatura": "Mix 171", "Foto": f"{GITHUB_RAW_BASE}/371.png", "Valore": 10},
    {"Creatura": "Mix 172", "Foto": f"{GITHUB_RAW_BASE}/372.png", "Valore": 10},
    {"Creatura": "Mix 173", "Foto": f"{GITHUB_RAW_BASE}/373.png", "Valore": 10},
    {"Creatura": "Mix 174", "Foto": f"{GITHUB_RAW_BASE}/374.png", "Valore": 10},
    {"Creatura": "Mix 175", "Foto": f"{GITHUB_RAW_BASE}/375.png", "Valore": 10},
    {"Creatura": "Mix 176", "Foto": f"{GITHUB_RAW_BASE}/376.png", "Valore": 10},
    {"Creatura": "Mix 177", "Foto": f"{GITHUB_RAW_BASE}/377.png", "Valore": 10},
    {"Creatura": "Mix 178", "Foto": f"{GITHUB_RAW_BASE}/378.png", "Valore": 10},
    {"Creatura": "Mix 179", "Foto": f"{GITHUB_RAW_BASE}/379.png", "Valore": 10},
    {"Creatura": "Mix 180", "Foto": f"{GITHUB_RAW_BASE}/380.png", "Valore": 10},
    {"Creatura": "Mix 181", "Foto": f"{GITHUB_RAW_BASE}/381.png", "Valore": 10},
    {"Creatura": "Mix 182", "Foto": f"{GITHUB_RAW_BASE}/382.png", "Valore": 10},
    {"Creatura": "Mix 183", "Foto": f"{GITHUB_RAW_BASE}/383.png", "Valore": 10},
    {"Creatura": "Mix 184", "Foto": f"{GITHUB_RAW_BASE}/384.png", "Valore": 10},
    {"Creatura": "Mix 185", "Foto": f"{GITHUB_RAW_BASE}/385.png", "Valore": 10},
    {"Creatura": "Mix 186", "Foto": f"{GITHUB_RAW_BASE}/386.png", "Valore": 10},
    {"Creatura": "Mix 187", "Foto": f"{GITHUB_RAW_BASE}/387.png", "Valore": 10},
    {"Creatura": "Mix 188", "Foto": f"{GITHUB_RAW_BASE}/388.png", "Valore": 10},
    {"Creatura": "Mix 189", "Foto": f"{GITHUB_RAW_BASE}/389.png", "Valore": 10},
    {"Creatura": "Mix 190", "Foto": f"{GITHUB_RAW_BASE}/390.png", "Valore": 10},
    {"Creatura": "Mix 191", "Foto": f"{GITHUB_RAW_BASE}/391.png", "Valore": 10},
    {"Creatura": "Mix 192", "Foto": f"{GITHUB_RAW_BASE}/392.png", "Valore": 10},
    {"Creatura": "Mix 193", "Foto": f"{GITHUB_RAW_BASE}/393.png", "Valore": 10},
    {"Creatura": "Mix 194", "Foto": f"{GITHUB_RAW_BASE}/394.png", "Valore": 10},
    {"Creatura": "Mix 195", "Foto": f"{GITHUB_RAW_BASE}/395.png", "Valore": 10},
    {"Creatura": "Mix 196", "Foto": f"{GITHUB_RAW_BASE}/396.png", "Valore": 10},
    {"Creatura": "Mix 197", "Foto": f"{GITHUB_RAW_BASE}/397.png", "Valore": 10},
    {"Creatura": "Mix 198", "Foto": f"{GITHUB_RAW_BASE}/398.png", "Valore": 10},
    {"Creatura": "Mix 199", "Foto": f"{GITHUB_RAW_BASE}/399.png", "Valore": 10},
    {"Creatura": "Mix 200", "Foto": f"{GITHUB_RAW_BASE}/400.png", "Valore": 10},
]

TOURNAMENTS = {
    "Torneo Creature Marine": MARINE_CREATURES,
    "Torneo Di Pesca": FISHING_CREATURES,
    "Torneo Caccia all'insetto": INSECT_CREATURES,
    "Torneo Mix": MIX_CREATURES,
}
if "creature_points" not in st.session_state:
    st.session_state.creature_points = 1
if "creature_rows" not in st.session_state:
    st.session_state.creature_rows = pd.DataFrame(columns=["Foto", "Valore", "Quantità", "Totale"])
if "active_hero_button" not in st.session_state:
    st.session_state.active_hero_button = ""
if "selected_tournament" not in st.session_state:
    st.session_state.selected_tournament = "Torneo Creature Marine"
if "custom_tournament_rows" not in st.session_state:
    st.session_state.custom_tournament_rows = pd.DataFrame(columns=["Foto", "Valore", "Quantità", "Totale"])
if "participant_slots" not in st.session_state:
    st.session_state.participant_slots = [
        {"selected": False, "name": ""}
        for _ in range(12)
    ]
if "selected_participant" not in st.session_state:
    st.session_state.selected_participant = ""
if "capture_data" not in st.session_state:
    st.session_state.capture_data = {}
if "last_tournament" not in st.session_state:
    st.session_state.last_tournament = None


def get_active_participants():
    active = []
    for slot in st.session_state.participant_slots:
        name = (slot.get("name") or "").strip()
        if slot.get("selected") and name:
            active.append(name)
    return active


def build_capture_frame(tournament_name):
    rows = []
    for index, item in enumerate(TOURNAMENTS.get(tournament_name, []), start=1):
        rows.append({
            "Creatura": item.get("Creatura", f"Creatura {index}"),
            "Foto": item.get("Foto", ""),
            "Valore": int(item.get("Valore", 0)),
            "Quantità": 0,
            "Totale": 0,
        })
    return pd.DataFrame(rows)


def make_image_cell(uploaded_file):
    if uploaded_file is None:
        return ""
    try:
        return uploaded_file.getvalue()
    except Exception:
        return str(uploaded_file)


def make_custom_rows_from_uploaded(uploaded_files, points):
    rows = []
    for uploaded_file in uploaded_files or []:
        if uploaded_file is not None:
            rows.append({
                "Foto": make_image_cell(uploaded_file),
                "Valore": int(points),
                "Quantità": 0,
                "Totale": 0,
            })
    return pd.DataFrame(rows, columns=["Foto", "Valore", "Quantità", "Totale"])


if st.session_state.selected_tournament != st.session_state.last_tournament:
    for participant in get_active_participants():
        st.session_state.capture_data[participant] = build_capture_frame(st.session_state.selected_tournament)
    st.session_state.last_tournament = st.session_state.selected_tournament

for participant in get_active_participants():
    if participant not in st.session_state.capture_data:
        st.session_state.capture_data[participant] = build_capture_frame(st.session_state.selected_tournament)

if st.session_state.selected_participant not in get_active_participants():
    active_participants = get_active_participants()
    st.session_state.selected_participant = active_participants[0] if active_participants else ""

st.markdown(
    """
    <style>
        .main {
            background: linear-gradient(180deg, #dffdfb 0%, #d7f7f8 30%, #f3fdfd 100%);
        }

        .hero {
            background: linear-gradient(135deg, rgba(12, 135, 154, 0.96), rgba(18, 190, 204, 0.82));
            border-radius: 24px;
            padding: 2.2rem 2.4rem;
            box-shadow: 0 14px 30px rgba(10, 94, 112, 0.18);
            border: 1px solid rgba(255,255,255,0.25);
            margin-bottom: 1.5rem;
        }

        .eyebrow {
            display: inline-block;
            background: rgba(255,255,255,0.15);
            color: #ecfeff;
            border: 1px solid rgba(255,255,255,0.25);
            border-radius: 999px;
            padding: 0.35rem 0.8rem;
            font-size: 0.76rem;
            font-weight: 700;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            margin-bottom: 1rem;
        }

        .hero h1 {
            color: white;
            font-size: 3rem;
            line-height: 1.1;
            margin: 0 0 0.8rem 0;
            font-weight: 800;
        }

        .hero p {
            color: rgba(255,255,255,0.9);
            font-size: 1.1rem;
            line-height: 1.6;
            max-width: 700px;
            margin: 0;
        }

        div.stButton > button {
            background: linear-gradient(135deg, #f8dcc0, #efbb7d) !important;
            color: #4d2f12 !important;
            border: 1px solid rgba(129, 92, 42, 0.25) !important;
            border-radius: 999px !important;
            padding: 0.5rem 0.9rem !important;
            font-size: 0.80rem !important;
            font-weight: 700 !important;
            box-shadow: 0 6px 18px rgba(198, 143, 83, 0.2) !important;
        }

        .glass {
            background: rgba(255,255,255,0.56);
            border: 1px solid rgba(13, 146, 167, 0.12);
            border-radius: 18px;
            padding: 1.2rem 1.1rem;
            box-shadow: 0 10px 24px rgba(20, 111, 130, 0.08);
            height: 100%;
        }

        .metric-card {
            background: linear-gradient(180deg, rgba(255,255,255,0.7), rgba(204,251,255,0.5));
            border: 1px solid rgba(12, 135, 154, 0.12);
            border-radius: 18px;
            padding: 1.15rem 1rem;
            text-align: center;
            box-shadow: 0 8px 22px rgba(15, 118, 140, 0.07);
            height: 100%;
        }

        .metric-card .value {
            font-size: 2rem;
            font-weight: 800;
            color: #0f8894;
            margin: 0;
        }

        .metric-card .label {
            font-size: 0.85rem;
            color: #1b5360;
            margin-top: 0.3rem;
            font-weight: 600;
        }

        .section-title {
            color: #0c5964;
            font-size: 1.6rem;
            font-weight: 800;
            margin: 1.8rem 0 1rem 0;
        }

        .feature-box {
            background: rgba(255,255,255,0.65);
            border: 1px solid rgba(9, 129, 146, 0.10);
            border-radius: 18px;
            padding: 1.2rem;
            box-shadow: 0 12px 25px rgba(8, 106, 122, 0.06);
            height: 100%;
        }

        .feature-box h3 {
            color: #0e5a66;
            margin-top: 0.3rem;
            margin-bottom: 0.5rem;
        }

        .feature-box p {
            color: #3f5c63;
            line-height: 1.6;
            margin: 0;
        }

        .icon {
            font-size: 1.8rem;
            display: block;
            margin-bottom: 0.4rem;
        }

        .score-box {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            background: linear-gradient(180deg, rgba(255,255,255,0.8), rgba(210,247,250,0.8));
            border: 1px solid rgba(12, 135, 154, 0.14);
            border-radius: 18px;
            padding: 1rem 0.75rem;
            box-shadow: 0 10px 22px rgba(18, 123, 140, 0.08);
            margin-top: 1rem;
            min-height: 120px;
            text-align: center;
        }

        .score-box .value {
            font-size: 2.1rem;
            font-weight: 800;
            color: #0d6d7b;
            line-height: 1.1;
        }

        .score-box .label {
            font-size: 0.82rem;
            color: #285863;
            font-weight: 700;
            margin-top: 0.4rem;
            letter-spacing: 0.02em;
        }

        .custom-item-card {
            display: flex;
            align-items: center;
            gap: 0.8rem;
            width: 100%;
            min-height: 72px;
            background: rgba(255,255,255,0.76);
            border: 1px solid rgba(12, 135, 154, 0.12);
            border-radius: 16px;
            padding: 0.65rem 0.8rem;
            margin-bottom: 0.65rem;
            box-shadow: 0 8px 20px rgba(18, 123, 140, 0.05);
        }

        .custom-item-card img {
            width: 58px;
            height: 58px;
            object-fit: cover;
            border-radius: 12px;
            border: 1px solid rgba(12, 135, 154, 0.15);
            background: #f0fbfc;
            flex-shrink: 0;
        }

        .custom-item-meta {
            display: flex;
            flex-direction: column;
            justify-content: center;
            gap: 0.18rem;
            color: #0e5a66;
            font-size: 0.82rem;
            font-weight: 700;
            min-width: 0;
            line-height: 1.25;
        }

        .custom-item-meta .name {
            font-size: 0.9rem;
            font-weight: 800;
            color: #0d5964;
            white-space: normal;
            word-break: break-word;
        }

        .custom-item-meta span {
            color: #447d8a;
            font-size: 0.74rem;
            font-weight: 700;
        }

        .mini-total {
            display: flex;
            align-items: center;
            justify-content: center;
            min-height: 54px;
            border-radius: 12px;
            background: linear-gradient(180deg, rgba(218,248,250,0.95), rgba(184,237,242,0.85));
            border: 1px solid rgba(12, 135, 154, 0.12);
            font-size: 1.05rem;
            font-weight: 800;
            color: #0d6d7b;
            width: 100%;
            margin-top: 0.35rem;
        }

        .compact-number {
            width: 100%;
        }

        div[data-testid="stNumberInput"] {
            width: 100% !important;
        }

        div[data-testid="stNumberInput"] > div {
            background: #f5c400 !important;
            border: 1px solid rgba(150, 110, 0, 0.6) !important;
            border-radius: 12px !important;
            box-shadow: inset 0 0 0 1px rgba(255, 255, 255, 0.25) !important;
        }

        div[data-testid="stNumberInput"] input {
            background: #f5c400 !important;
            color: #5c4300 !important;
            font-weight: 700 !important;
        }

        div[data-testid="stExpander"] {
            border: 1px solid rgba(12, 135, 154, 0.18) !important;
            border-radius: 18px !important;
            background: rgba(255,255,255,0.60) !important;
            box-shadow: 0 12px 24px rgba(20, 111, 130, 0.06) !important;
            overflow: hidden !important;
        }

        div[data-testid="stExpander"] > div {
            background: transparent !important;
        }

        div[data-testid="stDataFrame"],
        div[data-testid="stTable"] {
            overflow-x: auto !important;
            overflow-y: visible !important;
            max-height: none !important;
            height: auto !important;
            width: 100% !important;
        }

        div[data-testid="stDataFrame"] > div,
        div[data-testid="stTable"] > div {
            overflow: visible !important;
        }

        @media (max-width: 768px) {
            div[data-testid="stDataFrame"],
            div[data-testid="stTable"] {
                font-size: 0.82rem !important;
            }
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="hero">
        <div class="eyebrow">🌊 CUP OF THE ISLANDS</div>
        <h1>Il tuo torneo da sogno!</h1>
        <p>
            Organizza tornei, monitora i risultati e tieni sempre sotto controllo la classifica!
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

hero_labels = ["Tornei", "Classifiche", "Isole", "Eventi", "Invita", "Info"]
hero_columns = st.columns(len(hero_labels))

for col, label in zip(hero_columns, hero_labels):
    with col:
        clicked = st.button(label, key=f"hero_{label.lower()}", use_container_width=True)
        if clicked:
            st.session_state.active_hero_button = label

if st.session_state.active_hero_button == "Info":
    st.markdown('<div class="section-title">Cosa puoi fare</div>', unsafe_allow_html=True)
    features = [
        ("🏆", "Tornei dinamici", "Crea competizioni personalizzate, impostando regole, date e gruppi di partecipazione in pochi secondi."),
        ("📊", "Classifiche live", "Segui i punteggi in tempo reale e scopri subito chi guida la classifica generale."),
    ]
    feature_cols = st.columns(2)
    for col, (icon, title, text) in zip(feature_cols, features):
        with col:
            st.markdown(
                f"""
                <div class="feature-box">
                    <span class="icon">{icon}</span>
                    <h3>{title}</h3>
                    <p>{text}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown('<div class="section-title">Panoramica</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="glass">
            <h3 style="color:#0c5964; margin-top:0;">La tua isola, in ordine</h3>
            <p style="color:#3f5c63; line-height:1.7; margin:0;">
                Un sistema pensato per tenere organizzati tornei, classifiche e momenti speciali in un unico ambiente.
                Ogni sezione è progettata per essere chiara, veloce e adatta a chi vuole gestire tutto con pochi click.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

if st.session_state.active_hero_button == "Tornei":
    st.markdown('<div class="section-title">Tornei disponibili</div>', unsafe_allow_html=True)
    tournament_list = list(TOURNAMENTS.keys())
    selected_tournament = st.selectbox(
        "Seleziona un torneo",
        tournament_list,
        index=tournament_list.index(st.session_state.selected_tournament) if st.session_state.selected_tournament in tournament_list else 0,
    )
    st.session_state.selected_tournament = selected_tournament

    if selected_tournament == "Torneo Fai Da Te":
        st.markdown(
            """
            <div class="glass">
                <p style="color:#1f4f5d; font-weight:600; margin:0 0 0.7rem 0;">
                    Carica immagini, imposta il valore e scegli chi partecipa al torneo personalizzato.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        uploaded_files = st.file_uploader(
            "Carica foto PNG o JPEG",
            type=["png", "jpg", "jpeg"],
            accept_multiple_files=True,
            help="Puoi caricare più immagini e aggiungerle alla tabella del torneo.",
        )

        if uploaded_files:
            for uploaded_file in uploaded_files:
                if uploaded_file is not None:
                    st.image(uploaded_file, caption=uploaded_file.name, width=120)

        points_title = "<div style='margin-top: 1rem; color: #0c5964; font-weight: 700; font-size: 1.05rem;'>Valore Punti:</div>"
        st.markdown(points_title, unsafe_allow_html=True)

        points_col1, points_col2, points_col3 = st.columns([1, 2, 1])
        with points_col1:
            if st.button("-", key="custom_decrease_points", use_container_width=True):
                st.session_state.creature_points = max(0, st.session_state.creature_points - 1)
        with points_col2:
            st.markdown(
                f"<div style='text-align:center; padding: 0.7rem 0; border-radius: 12px; background: rgba(255,255,255,0.7); border: 1px solid rgba(12,135,154,0.15); font-size: 2rem; font-weight: 800; color: #0c5964;'>{st.session_state.creature_points}</div>",
                unsafe_allow_html=True,
            )
        with points_col3:
            if st.button("+", key="custom_increase_points", use_container_width=True):
                st.session_state.creature_points = st.session_state.creature_points + 1

        if uploaded_files and st.session_state.creature_points > 0 and st.session_state.custom_tournament_rows.empty:
            st.session_state.custom_tournament_rows = make_custom_rows_from_uploaded(uploaded_files, st.session_state.creature_points)

        if st.button("Aggiungi alla tabella in basso", use_container_width=True):
            new_rows = make_custom_rows_from_uploaded(uploaded_files, st.session_state.creature_points)
            if not new_rows.empty:
                st.session_state.custom_tournament_rows = pd.concat(
                    [st.session_state.custom_tournament_rows, new_rows],
                    ignore_index=True,
                )
                st.success("Immagini aggiunte alla tabella del torneo personalizzato!")
                st.session_state.creature_points = 1

        with st.expander("Partecipanti", expanded=False):
            st.markdown(
                "<div style='padding: 0.25rem 0 0.75rem 0; color: #1d5662; font-weight: 700;'>Seleziona i partecipanti attivi</div>",
                unsafe_allow_html=True,
            )
            for idx in range(12):
                slot = st.session_state.participant_slots[idx]
                checkbox_col, name_col = st.columns([0.35, 2.6])
                with checkbox_col:
                    slot["selected"] = st.checkbox("", value=slot.get("selected", False), key=f"custom_participant_selected_{idx}", label_visibility="collapsed")
                with name_col:
                    slot["name"] = st.text_input(
                        "",
                        value=slot.get("name", ""),
                        key=f"custom_participant_name_{idx}",
                        placeholder=f"Partecipante {idx + 1}",
                        label_visibility="collapsed",
                    )

        custom_table = st.session_state.custom_tournament_rows.copy()
        if not custom_table.empty:
            custom_table["Totale"] = custom_table["Valore"] * custom_table["Quantità"]
            custom_table = custom_table[["Foto", "Valore", "Quantità", "Totale"]]
            st.session_state.custom_tournament_rows = custom_table
            st.table(custom_table)

    with st.expander("Partecipanti", expanded=False):
        st.markdown(
            "<div style='padding: 0.25rem 0 0.75rem 0; color: #1d5662; font-weight: 700;'>Seleziona i partecipanti attivi</div>",
            unsafe_allow_html=True,
        )
        for idx in range(12):
            slot = st.session_state.participant_slots[idx]
            checkbox_col, name_col = st.columns([0.35, 2.6])
            with checkbox_col:
                slot["selected"] = st.checkbox("", value=slot.get("selected", False), key=f"participant_selected_{idx}", label_visibility="collapsed")
            with name_col:
                slot["name"] = st.text_input(
                    "",
                    value=slot.get("name", ""),
                    key=f"participant_name_{idx}",
                    placeholder=f"Partecipante {idx + 1}",
                    label_visibility="collapsed",
                )

    active_participants = get_active_participants()

    if not active_participants:
        st.warning("Seleziona almeno un partecipante attivo per continuare.")
    else:
        st.session_state.selected_participant = st.selectbox(
            "Partecipante attivo",
            active_participants,
            index=active_participants.index(st.session_state.selected_participant) if st.session_state.selected_participant in active_participants else 0,
        )

        selected_name = st.session_state.selected_participant
        if selected_name not in st.session_state.capture_data:
            st.session_state.capture_data[selected_name] = build_capture_frame(st.session_state.selected_tournament)

        table = st.session_state.capture_data[selected_name].copy()
        table["Totale"] = table["Valore"] * table["Quantità"]

        for idx, row in table.iterrows():
            quantity = int(row["Quantità"])
            quantity_key = f"qty_{selected_name}_{st.session_state.selected_tournament}_{idx}".replace(" ", "_")
            info_col, controls_col = st.columns([4.5, 1.8])

            with info_col:
                st.markdown(
                    f"""
                    <div class="custom-item-card">
                        <img src="{row['Foto']}" alt="{row['Creatura']}" />
                        <div class="custom-item-meta">
                            <div class="name">{row['Creatura']}</div>
                            <span>Valore: {int(row['Valore'])}</span>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            with controls_col:
                q_value = st.number_input(
                    "Q",
                    min_value=0,
                    step=1,
                    value=quantity,
                    key=quantity_key,
                    label_visibility="collapsed",
                )
                table.at[idx, "Quantità"] = int(q_value)

                total_value = int(row["Valore"] * q_value)
                table.at[idx, "Totale"] = total_value
                st.markdown(f"<div class=\"mini-total\">{total_value}</div>", unsafe_allow_html=True)

        st.session_state.capture_data[selected_name] = table

        total_creature_count = int(table["Quantità"].sum())
        total_points = int(table["Totale"].sum())
        qty_col, total_col = st.columns(2)
        with qty_col:
            st.markdown(
                f"""
                <div class="score-box">
                    <div class="value">{total_creature_count}</div>
                    <div class="label">Totale creature prese</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with total_col:
            st.markdown(
                f"""
                <div class="score-box">
                    <div class="value">{total_points}</div>
                    <div class="label">Totale punti</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

elif st.session_state.active_hero_button == "Classifiche":
    st.markdown('<div class="section-title">Classifica del torneo</div>', unsafe_allow_html=True)
    active_participants = get_active_participants()
    if not active_participants:
        st.warning("Nessun partecipante attivo. Seleziona i giocatori nel pannello Tornei.")
    else:
        leaderboard_rows = []
        for participant in active_participants:
            capture_df = st.session_state.capture_data.get(participant)
            if capture_df is None:
                capture_df = build_capture_frame(st.session_state.selected_tournament)
                st.session_state.capture_data[participant] = capture_df
            qty = int(capture_df["Quantità"].sum())
            total = int((capture_df["Valore"] * capture_df["Quantità"]).sum())
            leaderboard_rows.append({
                "Nome partecipante": participant,
                "Quantità": qty,
                "Totale punti": total,
            })

        leaderboard = pd.DataFrame(leaderboard_rows)
        leaderboard = leaderboard.sort_values(["Totale punti", "Quantità"], ascending=[False, False]).reset_index(drop=True)
        leaderboard.insert(0, "Posizione", range(1, len(leaderboard) + 1))
        leaderboard_display = leaderboard[["Posizione", "Nome partecipante", "Quantità", "Totale punti"]].copy()
        leaderboard_display["Totale punti"] = leaderboard_display["Totale punti"].map(int)
        st.table(leaderboard_display)

elif st.session_state.active_hero_button == "Eventi":
    st.markdown('<div class="section-title">Eventi</div>', unsafe_allow_html=True)
    cols = st.columns(4)
    metrics = [
        ("24", "Tornei attivi"),
        ("8.4k", "Partecipanti"),
        ("96%", "Engagement"),
        ("12", "Eventi in corso"),
    ]
    for col, (value, label) in zip(cols, metrics):
        with col:
            st.markdown(
                f'<div class="metric-card"><div class="value">{value}</div><div class="label">{label}</div></div>',
                unsafe_allow_html=True,
            )
    st.info("Qui potrai creare e gestire gli eventi del torneo.")

st.caption("Prototipo homepage - CUP OF THE ISLANDS")
