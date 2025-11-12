import streamlit as st
import base64
st.markdown(
    """<p style="text-align: justify;"><B>Dans cette page, vous pouvez consulter 
    les différentes projets sur lesquels j'ai travaillé pour mettre en 
    pratiques les connaissances acquisent au cours de mon cursus scolaire.</B></p>""",
    unsafe_allow_html=True,
)
col = st.columns(2)
# ===========ANALYSE DE DONNÉES==============

col[0].write(
    """<h2 align=right><FONT color="orange">Analyse de</FONT></h2>""",
    unsafe_allow_html=True,
)
col[1].write(
    """<h2 align=left><FONT color="orange">données</FONT></h2>""",
    unsafe_allow_html=True,
)
# ============Projet power BI==============

for i in range(1):
    col[0].write("\n")
col[0].write(
    """<h4 align=left><FONT color="orange">Dashboard avec power BI</FONT></h4>""",
    unsafe_allow_html=True,
)
for i in range(3):
    col[1].write("\n")
# Projet power BI M2SID
col[0].write(
    """
  <p style="text-align: justify;"><B>
 Dans cette étude, l'objectif est de metter en place
 un tableau de bord pour avoir une vue globale sur
 l'évolution des ventes. Pour
 ce fait nous avons procédé comme suite :<br>
 1- Charger les différents fichiers Excel dans Power BI et appliquer les transformations et les nettoyages que nous trouvons nécessaire pour une meilleure analyse des données.<br>
 2- Générer une table de dimension calendrier.<br>
 3- Créer des mesures et des graphes que nous trouvons pertinents et réaliser un Dashboard 
 convivial et dynamique avec des filtres sur les données.<br>
 </B></p>
 """,
    unsafe_allow_html=True,
)
for i in range(2):
    col[1].write("\n")
col[1].image("static/Dashbord ventes.jpg", use_column_width=True)

col[1].link_button(
    "Plus info",
    url="",
)

# Tableau de bord ID GLOBAL BUSNESS
for i in range(3):
    col[1].write("\n")
with open("doc/Curriculum_vitae_Malick_FAYE.pdf", "rb") as pdf_file:
    pdf = pdf_file.read()
col[1].write(
    """
  <p style="text-align: justify;"><B>
  interprétation peut conduire à des décisions erronées.<br><br>
    L'objectif de ce document est de présenter les concepts fondamentaux du traitement de données, 
    les méthodes couramment utilisées et les outils disponibles pour faciliter ce processus. Une base 
    issue de l’ANSD (Agence Nationale de la Statistique et de la Démographie) 
    sera utilisée dans ce travail pour montrer les différentes étapes du traitement de donnée.<br>
 </B></p>
 """,
    unsafe_allow_html=True,
)
for i in range(1):
    col[1].write("\n")
col[0].write(
    """
  <p style="text-align: justify;"><B>
 Dans un monde où les données sont produites en quantité exponentielle, leur traitement efficace est devenu 
 un enjeu majeur pour les entreprises, les chercheurs et les institutions. Le traitement de données consiste 
 à collecter, organiser, analyser et interpréter des informations brutes afin de les transformer en connaissances 
 exploitables. Le processus de traitement de données comprend plusieurs étapes clés : la collecte, le nettoyage, 
 l'analyse et la visualisation. Chacune de ces étapes joue un rôle crucial dans la garantie de la qualité et de 
 la pertinence des résultats obtenus. Par exemple, des données mal nettoyées 
 peuvent fausser les analyses, tandis qu'une mauvaise<br>
 </B></p>
 """,
    unsafe_allow_html=True,
)
pdf_path = "doc/Curriculum_vitae_Malick_FAYE.pdf"
# Lecture du PDF
if col[1].button("Plus info", key="download_report"):
    with open(pdf_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    # Affichage dans Streamlit via iframe
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="1000" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)


# Projet Intégration de données
for i in range(1):
    col[0].write("\n")
col[0].write(
    """
  <p style="text-align: justify;"><B>
 Dans cette étude, l'objectif est de metter en place
 un tableau de bord pour avoir une vue globale sur l'évolution des gains de médailles au niveau du jeux Olympique.
 Pour cela, le jeu de données Summer_Olympic_medallists_1896-2008 est mis à votre disposition. Il fournit les médaillés
des Jeux olympiques de chaque été entre 1896 et 2012<br>
 </B></p>
 """,
    unsafe_allow_html=True,
)
for i in range(3):
    col[1].write("\n")
col[1].image("static/Dashbord medailles.jpg", use_column_width=True)

col[0].link_button(
    "Plus info",
    url="https://app.powerbi.com/links/cCsOthnxzo?ctid=0864d57d-5a5e-4244-8b08-b03f4166a67a&pbi_source=linkShare&bookmarkGuid=e16b0720-399c-4197-9702-4d93f8698eac",
)
# =============Projet excel=============

for i in range(6):
    col[1].write("\n")
col[0].write(
    """<h4 align=left><FONT color="orange">Dashboard RNU Excel</FONT></h4>""",
    unsafe_allow_html=True,
)

col[1].write(
    """
    <p style="text-align: justify;"><B>
    l'évolution des enquetes au près de l'ensemble des ménages des 
    quatre (4) communes du département de Kaffrine. L'objectif de ce travail est d'avoir 
    une vue globale sur la progression des enquetes au près des ménages pour mener à bien la
    réalisation du projet d'enquete dans le cadre de la mise à jours et extention
    du Registre National Unique (RNU).
    Ce travail consiste à mettre en place un tableau de bord qui va nous permetre de suivre en temps réel 
    </B></p>
    """,
    unsafe_allow_html=True,
)
col[0].image("static/Departement de Kaffine.jpg")
# Modèélisation des données avec python

for i in range(2):
    col[0].write("\n")
col[0].write(
    """<h2 align=right><FONT color="orange">Modélisation avec</FONT></h2>""",
    unsafe_allow_html=True,
)
col[1].write(
    """<h2 align=left><FONT color="orange">Python</FONT></h2>""",
    unsafe_allow_html=True,
)

# =============Projets Biostatistiques=======================

for i in range(5):
    col[1].write("\n")
col[0].write(
    """<h4 align=left><FONT color="orange">Biostatistique</FONT></h4>""",
    unsafe_allow_html=True,
)
col[0].write(
    """
    <p style="text-align: justify;"><B>
    Le projet de Biostatistique consiste à mettre en place un modèle de machine 
    learning ou statistique qui permet de faire un pronostique sur 
    la survenue instantanée de décès après le traitement.Pour la 
    construction de ce modèle, nous avons utiliser les données des patients 
    atteints d’accident cérébral vasculaire (AVC), traités et suivis.
    </B></p>
    """,
    unsafe_allow_html=True,
)
col[1].image("static/biosta.jpeg")
col[0].link_button("Plus info", url="https://projetbiostatistique.streamlit.app")

for i in range(3):
    col[0].write("\n")
for i in range(1):
    col[1].write("\n")

# ========Projet Series Temporelles=================
col[1].write(
    """<h4 align=left><FONT color="orange">Série Temporelle</FONT></h4>""",
    unsafe_allow_html=True,
)
col[1].write(
    """
    <p style="text-align: justify;"><B>
    Les objectifs attendus dans cette étude sont nombreux.
    Parmi lesquelles, nous pouvons citer tout d’abord, 
    l’étude de la tendance de la série en utilisant un 
    modèle linéaire simple et multiple. Ensuite de faire 
    une prédiction de la production électrique pour les 
    années à venir en utilisant les processus ARIMA et la 
    méthode de lissage exponentiel et enfin de fournir des résultats 
    fiables qui pourrons aider les décideurs à prendre des décisions éclairées 
    sur la production d’électrique.
    </B></p>
    """,
    unsafe_allow_html=True,
)
col[0].image("static/series temporelles.png")
col[0].write(
    """
    <p style="text-align: justify;"><B>
    Dans cette étude, nous allons à modéliser les données de la 
    production électrique mensuelle d’un pays entre 1985 et 2018.
    </B></p>
    """,
    unsafe_allow_html=True,
)
# col[1].link_button(
#   "Plus info",
#  url="",
# )

# ===============Développement d'application===========================
for i in range(1):
    col[0].write("\n")
col[0].write(
    """<h2 align=right><FONT color="orange">Développement </FONT></h2>""",
    unsafe_allow_html=True,
)
col[1].write(
    """<h2 align=left><FONT color="orange">d'Application</FONT></h2>""",
    unsafe_allow_html=True,
)
for i in range(5):
    col[1].write("\n")
# ===============Application python===========================
col[0].write(
    """<h4 align=left><FONT color="orange">Application Python</FONT></h4>""",
    unsafe_allow_html=True,
)
col[0].write(
    """
    <p style="text-align: justify;"><B>
    Cette étude consiste à mettre en place une application Arithmanceur.
    L’arithmancie ou l’arithmomancie est une technique de divination basée 
    sur les nombres de 1 à 9.Le plus souvent, il s’agit de transformer le 
    prénom et le nom des gens en une suite de chiffres pour
    obtenir ce qu’on appelle le nombre d’expression, le nombre intime et 
    le nombre de réalisation. Chacun de ces nombres est ensuite analysé.
    Pour ce fair, nous allons faire un contrôle de saisie pour gérer les 
    entrées de l’utilisateur. Nous forcerons aussi l’utilisateur à entrer 
    une chaîne de caractère comportant uniquement
    l’alphabet latin (a - z) ou (A - Z).
    </B></p>
    """,
    unsafe_allow_html=True,
)
col[1].image("static/arithmacie.jpg")
col[1].write("\n")
# col[1].link_button(
#   "Plus info",
#  url="",
# )
