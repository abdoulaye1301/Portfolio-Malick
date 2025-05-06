# Importation des bibliothéques
import streamlit as st
from pathlib import Path

# Page du projet
accueil = st.Page(
    page="views/Accueille.py",
    title="A propos",
    default=True,
)
competence = st.Page(
    page="views/Qualifications.py",
    title="Qualifications & Expériences",
    icon="",
)
projet = st.Page(
    page="views/Projets.py",
    title="Projets",
    icon="",
)
skills = st.Page(
    page="views/Skills.py",
    title="Logiciels",
    icon="",
)
# contact = st.Page(page="views/Contacts.py", title="Contacts", icon="")
# Navigation des pages
pg = st.navigation(
    {
        "Information": [accueil],
        "Réalisation": [competence, skills, projet],
    }
)

dire = Path(__file__).parent if "__file__" in locals() else Path.cwd()
fichier_css = "views/fichier.css"
titre_page = "Abdoulaye NDAO"
icone_page = "static/Plan de travail 1.png"
with open(fichier_css) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

# Configuration de page

st.logo(icone_page)
pg.run()
