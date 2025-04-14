
import streamlit as st
from PIL import Image

# Logo
logo_path = "1E9914E6-CED5-4772-B62C-1E14D1360F9E.jpeg"

# Langues disponibles
languages = {
    "Français": {
        "title": "Calcul de longueur Inox-Mn (en mm)",
        "select_program": "Sélectionne un programme Inox-Mn :",
        "soude": "Longueur du cœur soudé (LS) en mm",
        "usine": "Longueur du cœur usiné (LU) en mm",
        "results": "Résultats",
        "antenne": "Longueur antenne avec inox",
        "rail": "Longueur du rail à couper",
        "inox": "Longueur inox",
        "prog_rail": "Programme Rail-Inox",
        "select_lang": "Langue"
    },
    "English": {
        "title": "Inox-Mn Length Calculator (mm)",
        "select_program": "Select an Inox-Mn Program:",
        "soude": "Welded heart length (LS) in mm",
        "usine": "Machined heart length (LU) in mm",
        "results": "Results",
        "antenne": "Length with inox antenna",
        "rail": "Length of rail to cut",
        "inox": "Inox length",
        "prog_rail": "Rail-Inox Program",
        "select_lang": "Language"
    },
    "Español": {
        "title": "Calculadora de Longitud Inox-Mn (mm)",
        "select_program": "Selecciona un programa Inox-Mn:",
        "soude": "Longitud del corazón soldado (LS) en mm",
        "usine": "Longitud del corazón mecanizado (LU) en mm",
        "results": "Resultados",
        "antenne": "Longitud con antena de inox",
        "rail": "Longitud del riel a cortar",
        "inox": "Longitud de inox",
        "prog_rail": "Programa Rail-Inox",
        "select_lang": "Idioma"
    },
    "Română": {
        "title": "Calculator Lungime Inox-Mn (mm)",
        "select_program": "Selectează un program Inox-Mn:",
        "soude": "Lungime inimă sudată (LS) în mm",
        "usine": "Lungime inimă prelucrată (LU) în mm",
        "results": "Rezultate",
        "antenne": "Lungime cu antenă inox",
        "rail": "Lungimea șinei de tăiat",
        "inox": "Lungime inox",
        "prog_rail": "Program Rail-Inox",
        "select_lang": "Limbă"
    }
}

# Données programmes (en mm)
data = [
    {
        "Programme Inox-Mn": "SNCF 227-60E1 ",
        "coef 1": 26.6,
        "coef 2": 7.6,
        "Longueur inox": 32.0,
        "Programme Rail-Inox": "300-60E1 Rail/Inox(300)"
    },
    {
        "Programme Inox-Mn": "229-115RE Inox Manganese(229)",
        "coef 1": 27.8,
        "coef 2": 18.8,
        "Longueur inox": 20.0,
        "Programme Rail-Inox": "115 RE 405"
    },
    {
        "Programme Inox-Mn": "230-132RE Inox/Mn 30 mm(230)",
        "coef 1": 26.7,
        "coef 2": 20.0,
        "Longueur inox": 20.0,
        "Programme Rail-Inox": "408-132RE Rail/Inox(408)"
    },
    {
        "Programme Inox-Mn": "232-56E1 R260 (232)",
        "coef 1": 28.9,
        "coef 2": 3.0,
        "Longueur inox": 37.0,
        "Programme Rail-Inox": "401-56E1 Rail/Inox Post Heating(401)"
    },
    {
        "Programme Inox-Mn": "SNCF 241-50E6 ",
        "coef 1": 22.7,
        "coef 2": 7.6,
        "Longueur inox": 27.0,
        "Programme Rail-Inox": "410-50 E6 SNCF(410)"
    },
    {
        "Programme Inox-Mn": "750-RFI Inox/Mn 60E1(750)",
        "coef 1": 22.8,
        "coef 2": 16.4,
        "Longueur inox": 20.0,
        "Programme Rail-Inox": "480-RFI Rail R260/Inox 60E1(480)"
    },
    {
        "Programme Inox-Mn": "INFRABEL BWG 227-60E1 ",
        "coef 1": 26.6,
        "coef 2": 15.8,
        "Longueur inox": 24.0,
        "Programme Rail-Inox": "404-60E1 E2 Infrabel-BWG(404)"
    },
    {
        "Programme Inox-Mn": "INFRABEL 241-50E2",
        "coef 1": 22.7,
        "coef 2": 10.1,
        "Longueur inox": 24.0,
        "Programme Rail-Inox": "407-50kg ph(407)"
    },
    {
        "Programme Inox-Mn": "HP - 232-56E1",
        "coef 1": 28.9,
        "coef 2": 1.0,
        "Longueur inox": 39.0,
        "Programme Rail-Inox": "405-54kg 56kgRailHP/Inox Postheat(405)"
    },
    {
        "Programme Inox-Mn": "Network 60 E2 - 227",
        "coef 1": 26.6,
        "coef 2": 2.8,
        "Longueur inox": 37.0,
        "Programme Rail-Inox": "421 - 54 E1 ADIF"
    },
    {
        "Programme Inox-Mn": "260 ADIF 54 E1",
        "coef 1": 23.7,
        "coef 2": 18.3,
        "Longueur inox": 20.0,
        "Programme Rail-Inox": "404 - 60 E2 Network"
    }
]

st.set_page_config(page_title="Inox-Mn Calculator", layout="centered")

# Choix de la langue
lang = st.sidebar.selectbox("Lang / Idioma / Limbă", list(languages.keys()))
txt = languages[lang]

# Logo + Titre
col_logo, col_title = st.columns([1, 4])
with col_logo:
    st.image(logo_path, width=100)
with col_title:
    st.title(txt["title"])

# Sélection du programme
programme_options = {item["Programme Inox-Mn"].strip(): item for item in data}
programme_selected = st.selectbox(txt["select_program"], list(programme_options.keys()))

# Entrées utilisateur
longueur_soude = st.number_input(txt["soude"], min_value=0, step=1)
longueur_usine = st.number_input(txt["usine"], min_value=0, step=1)

# Résultats
if programme_selected and longueur_soude and longueur_usine:
    item = programme_options[programme_selected]
    coef1 = item["coef 1"]
    coef2 = item["coef 2"]

    longueur_antenne = longueur_soude - longueur_usine + coef1
    longueur_rail = longueur_soude - longueur_usine + coef2

    st.subheader(txt["results"])
    col1, col2 = st.columns(2)
    with col1:
        st.success(f"**{txt['antenne']}** : {longueur_antenne} mm")
        st.info(f"**{txt['inox']}** : {item['Longueur inox']} mm")
    with col2:
        st.success(f"**{txt['rail']}** : {longueur_rail} mm")
        st.info(f"**{txt['prog_rail']}** : {item['Programme Rail-Inox']}")
