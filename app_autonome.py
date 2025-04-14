
import streamlit as st

# Données intégrées
data = [
    {'Programme Inox-Mn': 'SNCF 227-60E1 ', 'coef 1': 26.6, 'coef 2': 7.6, 'Longueur inox': 32, 'Programme Rail-Inox': '300-60E1 Rail/Inox(300)'},
    {'Programme Inox-Mn': '229-115RE Inox Manganese(229)', 'coef 1': 27.8, 'coef 2': 18.8, 'Longueur inox': 20, 'Programme Rail-Inox': '115 RE 405'}
    # Ajoute ici toutes les autres entrées si besoin
]

st.title("Calcul des longueurs - Programme Inox-Mn")

programme_options = {item["Programme Inox-Mn"]: item for item in data}
programme_selected = st.selectbox("Sélectionne un programme Inox-Mn :", list(programme_options.keys()))

longueur_soude = st.number_input("Longueur du cœur soudé (LS)", min_value=0.0, step=0.1)
longueur_usine = st.number_input("Longueur du cœur usiné (LU)", min_value=0.0, step=0.1)

if programme_selected and longueur_soude and longueur_usine:
    item = programme_options[programme_selected]
    coef1 = item["coef 1"]
    coef2 = item["coef 2"]

    longueur_antenne = longueur_soude - longueur_usine + coef1
    longueur_rail = longueur_soude - longueur_usine + coef2

    st.subheader("Résultats")
    st.write(f"**Longueur antenne avec inox** : {longueur_antenne:.2f} m")
    st.write(f"**Longueur du rail à couper** : {longueur_rail:.2f} m")
    st.write(f"**Longueur inox** : {item['Longueur inox']} m")
    st.write(f"**Programme Rail-Inox** : {item['Programme Rail-Inox']}")
