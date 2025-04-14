
import streamlit as st
from PIL import Image

# Chargement du logo
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

# Données intégrées (en mm)
data = {data_dict_full}

st.set_page_config(page_title="Inox-Mn Calculator", layout="centered")

# Sélection de la langue
lang = st.sidebar.selectbox("Lang / Idioma / Limbă", list(languages.keys()))
txt = languages[lang]

# Logo et titre
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

# Affichage des résultats
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
