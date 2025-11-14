# Importation des bibliothéques
import streamlit as st
from pathlib import Path
from PIL import Image
from views.Contacts import contact_form

# les chemins des fichienrs
dire = Path(__file__).parent if "__file__" in locals() else Path.cwd()
fichier_css = dire / "fichier.css"
cv = "doc/Curriculum_vitae_Malick_FAYE.pdf"
icone_page = "static/Plan de travail 1.png"
linked = "static/linkedin.png"
gith = "static/github.png"
twitt = "static/twitter.png"
icone_cv = "static/cv.png"
titre_page = "Malick FAYE"
mail = "malickfaye66805@gmail.com"
tel = "07 59 05 98 50"
description = """ Data Scientist | Data Analyst | BI"""
media = {
    "LinkedIn": "https://www.linkedin.com/in/malick-faye-594829259/",
    "Twitter": "https://twitter.com/MalickFaye11",
    "E-mail": "malickfaye66805@gmail.com",
    "Github": "https://github.com/Malick668",
}


# Formulaire de contact
@st.dialog("Contacter moi")
def affiche_formulaire():
    contact_form()


# Chargement de la page CSS, CV
with open(fichier_css) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(cv, "rb") as pdf_file:
    pdf = pdf_file.read()
profil = Image.open(icone_page)

# Configuration de page
# st.set_page_config(page_title=titre_page, page_icon=profil, layout="wide")
logos = st.logo(profil)

col = st.columns(2, gap="small", vertical_alignment="center")
with col[0]:
    st.image(profil, width=300)
with col[1]:
    st.title(titre_page, anchor=False)
    st.write(description)
    st.write("☎️ ", tel)
    st.write("✉️ ", mail)
    st.download_button(
        label="📄Curriculum vitae",
        data=pdf,
        file_name=f"{titre_page}.pdf",
        mime="Application/octet-stream",
    )
##   if st.button("📤 Contacter moi"):
#     affiche_formulaire()
# st.write("")

st.write("\n\n")
st.markdown(
    """<p style="text-align: justify;"><B>
    Étudiant en Master 2 Ingénierie Mathématique pour la Science des Données à 
    l'Université de Lorraine, je recherche un stage de fin d'études à partir du 
    mois d'Avril dans les domaines de la data science, l'analyse de données ou l'ingénierie 
    des données. Fort d'une expérience en statistique publique et maitrise des outils 
    modernes d'analyse, je souhaite contribuer à des projets innovants de valorisation 
    des données.
        <br>
        <br>""",
    unsafe_allow_html=True,
)

# Page linkdin
cols = st.columns(len(media))
for i, (platforme, lien) in enumerate(media.items()):
    cols[i].write(f"[{platforme}]({lien})")
# colss = st.columns(4, vertical_alignment="center")
# colss[0].image(linked, width=70)
# colss[1].image(gith, width=70)
# colss[2].image(twitt, width=70)
# colss[len(media)].image(icone_cv, width=80)
linkedin = "https://raw.githubusercontent.com/sahirmaharaj/exifa/main/img/linkedin.gif"
twitter = "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExYjhueW1qZzYzZ2tmNXU0ZW5ncHppeGd3YXM3ZmJ3NWtsZ3BtaWp5MyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/rwfMYnhkW9leBRxHqD/giphy.gif"
email = "https://raw.githubusercontent.com/sahirmaharaj/exifa/main/img/email.gif"
github = "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExcDg3b2lwZnlseHdwdHcxenJtaDJlcGpod2ZsN2NxMjJiandhN2VlayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/du3J3cXyzhj75IOgvA/giphy.gif"


st.caption(
    f"""
        <div style='display: flex; align-items: center;'>
            <a href = 'https://www.linkedin.com/in/malick-faye-594829259/'><img src='{linkedin}' style='width: 70px; height: 70   px; margin-right: 110px;'></a>
            <a href = ''><img src='{twitter}' style='width: 70px; height: 70px; margin-right: 110px;'></a>
            <a href = 'mailto:{mail}'><img src='{email}' style='width: 70px; height: 70px; margin-right: 110px;'></a>
            <a href = 'https://github.com/Malick668'><img src='{github}' style='width: 70px; height: 70px;'></a>
            
        </div>
        """,
    unsafe_allow_html=True,
)
