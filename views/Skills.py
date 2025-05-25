import streamlit as st

st.markdown(
    """<p style="text-align: justify;"><B>Dans cette page, je vous présente les différents logiciels dont j'utilise le plus dans le cadre de 
    mes projets. De ce fait, j'ai énuméré ces logiciels par groupe de façon qu'ils soient plus lisibles et 
    plus compréhensif.</B></p>""",
    unsafe_allow_html=True,
)

# =========Outils de Infographie=======

st.write(
    """<h2 align=right><FONT color="orange">Outils d'intégration de données</FONT></h2>""",
    unsafe_allow_html=True,
)

# Talend Opend Studio
for i in range(3):
    st.write("\n")
st.image("static/talend.png", use_column_width=True)
st.write("\n")
st.write(
    """<p style="text-align: justify;"><B>Talend Open Studio (TOS) était 
    une suite d'outils open source proposée par Talend, une entreprise 
    spécialisée dans les solutions de gestion de données. Il offrait des 
    fonctionnalités d'intégration de données, de qualité des données, 
    de gestion de données de référence et d'intégration de services.</B>
    </p>""",
    unsafe_allow_html=True,
)

# =============LOGICIELS=======================

st.write("\n")
col = st.columns(2)

# MySQL
col[0].write(
    """<h2 align=right><FONT color="orange">Outils de gestion de</FONT></h2>""",
    unsafe_allow_html=True,
)
col[1].write(
    """<h2 align=left><FONT color="orange">bases de données</FONT></h2>""",
    unsafe_allow_html=True,
)
col[0].image("static/mySQL.png", use_column_width=True)
col[0].write(
    """<p style="text-align: justify;"><B>MySQL est un système de gestion de bases de données relationnelles (SGBDR) open source. Il permet de stocker, organiser et manipuler des 
    données en utilisant le langage SQL (Structured Query Language).</B></p>
    """,
    unsafe_allow_html=True,
)

# PostegreSQL
for i in range(3):
    col[1].write("\n")
col[1].image("static/postegre.png", use_column_width=True)
col[1].write(
    """<p style="text-align: justify;"><B>PostgreSQL est un système de gestion de bases 
    de données relationnelles (SGBDR) open source, réputé 
    pour sa puissance, sa flexibilité et sa conformité aux 
    standards SQL. Il est conçu pour gérer des bases de données de grande taille avec 
    un haut niveau de performance et de sécurité.</B></p>
    """,
    unsafe_allow_html=True,
)

# =========Outils de visualisations=======
for i in range(4):
    col[0].write("\n")
col[0].write(
    """<h2 align=right><FONT color="orange">Outils de</FONT></h2>""",
    unsafe_allow_html=True,
)
for i in range(3):
    col[1].write("\n")
col[1].write(
    """<h2 align=left><FONT color="orange">visualisations</FONT></h2>""",
    unsafe_allow_html=True,
)
# Excel

col[0].image("static/Excel.png", width=200)
col[0].write(
    """<p style="text-align: justify;"><B>Excel est un logiciel de tableur développé par Microsoft, 
    permettant de créer, organiser, analyser et visualiser des données
    sous forme de tableaux. Il est utilisé pour effectuer des calculs,
    gérer des bases de données, créer des graphiques et 
    automatiser des tâches à l'aide de macros et de VBA (Visual Basic for Applications).</B>
    </p>""",
    unsafe_allow_html=True,
)

# Power BI
col[1].image("static/power.png", width=240)
col[1].write(
    """<p style="text-align: justify;"><B>Power BI est un outil de business 
    intelligence (BI) développé par Microsoft, qui permet de collecter, 
    analyser et visualiser des données à partir de différentes sources. 
    Il aide les entreprises et les analystes à créer des tableaux de bord interactifs 
    et des rapports dynamiques pour mieux comprendre leurs données.</B></p>
    """,
    unsafe_allow_html=True,
)

# Tableau Desktop
for i in range(3):
    col[0].write("\n")
col[0].image("static/tableau.png", width=260)
for i in range(3):
    col[0].write("\n")
col[0].write(
    """<p style="text-align: justify;"><B>Tableau Desktop est un logiciel
    de visualisation de données qui permet de créer des tableaux de bord 
    interactifs et des rapports dynamiques à partir de différentes sources 
    de données. Il est largement utilisé en business intelligence (BI) et en analyse de 
    données pour explorer et comprendre visuellement les informations.</B>
    </p>""",
    unsafe_allow_html=True,
)

# SPSS
col[1].image("static/SPSS.png", width=170)
col[1].write(
    """<p style="text-align: justify;"><B>SPSS est un progiciel statistique 
    puissant qui offre un large éventail de fonctionnalités pour l'analyse, 
    la gestion et la visualisation des données. Il est largement utilisé dans 
    la recherche universitaire, ainsi que par les entreprises et les agences 
    gouvernementales pour analyser des ensembles de données complexes et 
    générer des informations qui peuvent aider à la prise de décision.</B></p>
    """,
    unsafe_allow_html=True,
)

# R
for i in range(3):
    col[0].write("\n")
col[0].image("static/R.png", width=200)

col[1].write(
    """<p style="text-align: justify;"><B>R est un langage de 
    programmation et un environnement logiciel principalement 
    utilisé pour l'analyse statistique, la visualisation de 
    données et la modélisation statistique. Il est particulièrement 
    populaire dans les domaines de la data science, de 
    l’analyse statistique et de l’apprentissage automatique.</B>
    </p>""",
    unsafe_allow_html=True,
)

# =========Outils de Programmation=======
for i in range(1):
    col[0].write("\n")
col[0].write(
    """<h2 align=right><FONT color="orange">Langages de</FONT></h2>""",
    unsafe_allow_html=True,
)
for i in range(2):
    col[1].write("\n")
col[1].write(
    """<h2 align=left><FONT color="orange">programmation</FONT></h2>""",
    unsafe_allow_html=True,
)

# Python

col[0].image("static/python.png", width=200)
col[0].write(
    """<p style="text-align: justify;"><B>Python est un langage de 
    programmation polyvalent et open-source, connu pour sa simplicité, 
    sa lisibilité et sa puissance. Il est utilisé dans de nombreux domaines 
    comme le développement web, la data science, 
    l'intelligence artificielle, l'automatisation et la cybersécurité.</B>
    </p>""",
    unsafe_allow_html=True,
)

# Java
col[1].image("static/java.png", width=150)
col[1].write(
    """<p style="text-align: justify;"><B>Java est un langage de programmation 
    orienté objet, robuste et multiplateforme, développé par Sun Microsystems 
    (aujourd’hui Oracle). Il est utilisé pour développer des 
    applications web, mobiles (Android), de bureau et d’entreprise.</B></p>
    """,
    unsafe_allow_html=True,
)

# HTML
for i in range(2):
    col[0].write("\n")
col[0].image("static/HTML.png", width=150)
col[0].write(
    """<p style="text-align: justify;"><B>HTML (HyperText Markup Language) 
    est le langage standard utilisé pour structurer et afficher du contenu 
    sur le web. Il utilise des balises (tags) pour organiser le texte, 
    les images, les liens, les vidéos et d'autres éléments d'une page web.</B>
    </p>""",
    unsafe_allow_html=True,
)

# CSS
col[1].image("static/CSS.png", width=150)
col[1].write(
    """<p style="text-align: justify;"><B>Le CSS (Cascading Style Sheets) est un 
    langage informatique utilisé pour décrire la présentation des documents HTML et 
    XML. Il permet de mettre en forme le texte contenu sur les pages web et est utilisé pour 
    définir les styles visuels tels que la couleur, la police, la mise en page, etc.</B></p>
    """,
    unsafe_allow_html=True,
)

# C
for i in range(2):
    col[0].write("\n")
col[0].image("static/c.png", width=200)
for i in range(2):
    col[0].write("\n")
col[0].write(
    """<p style="text-align: justify;"><B>Le langage C est un langage de programmation 
    généraliste, impératif et procédural, 
    développé dans les années 1970 par Dennis Ritchie au sein des laboratoires Bell.</B>
    </p>""",
    unsafe_allow_html=True,
)

# C++
col[1].image("static/c++.png", width=150)
col[1].write(
    """<p style="text-align: justify;"><B>C++ est un langage de programmation orienté objet, 
    développé par Bjarne Stroustrup au début des années 1980. Il est une extension du langage 
    C, ajoutant des fonctionnalités telles que les classes, l'héritage, le polymorphisme et 
    l'encapsulation. C++ est largement utilisé pour le développement de logiciels systèmes, 
    de jeux vidéo, d'applications 
    de bureau, et de systèmes embarqués, grâce à sa performance et sa flexibilité.</B></p>
    """,
    unsafe_allow_html=True,
)

# SQL
for i in range(2):
    col[0].write("\n")
col[0].image("static/sql.png", width=200)
col[0].write(
    """<p style="text-align: justify;"><B>SQL (Structured Query Language) 
    est un langage de programmation standardisé utilisé pour gérer et 
    interroger des bases de données relationnelles. Il permet de créer, modifier, 
    et manipuler les données stockées dans une base de données.</B>
    </p>""",
    unsafe_allow_html=True,
)

# Scala
col[1].image("static/scala.png", width=150)
col[1].write(
    """<p style="text-align: justify;"><B>Scala est un langage de 
    programmation moderne qui combine des caractéristiques de la 
    programmation fonctionnelle et de la programmation orientée objet. 
    Il est conçu pour être à la fois concis, expressif et 
    évolutif, tout en étant entièrement compatible avec Java.</B></p>
    """,
    unsafe_allow_html=True,
)

# =========Outils de Développement=======
for i in range(1):
    col[0].write("\n")
col[0].write(
    """<h2 align=right><FONT color="orange">Framworks de</FONT></h2>""",
    unsafe_allow_html=True,
)
for i in range(1):
    col[1].write("\n")
col[1].write(
    """<h2 align=left><FONT color="orange">développement</FONT></h2>""",
    unsafe_allow_html=True,
)

# Symfony
for i in range(1):
    col[0].write("\n")
col[0].image("static/Symfony.png", use_column_width=True)
col[0].write(
    """<p style="text-align: justify;"><B>Symfony est un framework 
    PHP open-source destiné à développer des applications web et 
    des sites web robustes, flexibles et évolutifs. Il suit le modèle 
    MVC (Modèle-Vue-Contrôleur) et est connu 
    pour sa modularité et sa réutilisabilité de composants.</B>
    </p>""",
    unsafe_allow_html=True,
)

# Streamlit
for i in range(1):
    col[1].write("\n")
col[1].image("static/streamlit.jpeg", use_column_width=True)
col[1].write(
    """<p style="text-align: justify;"><B>Streamlit est un 
    framework open-source en Python permettant de créer 
    facilement des applications web interactives pour la 
    visualisation de données et le machine learning, sans 
    avoir à se soucier du développement front-end. Il est 
    conçu pour être simple et rapide, et permet aux utilisateurs de 
    créer des interfaces web en quelques lignes de code.</B></p>
    """,
    unsafe_allow_html=True,
)

# =========Outils de Infographie=======

col[0].write(
    """<h2 align=right><FONT color="orange">Outils</FONT></h2>""",
    unsafe_allow_html=True,
)

col[1].write(
    """<h2 align=left><FONT color="orange">d'Infographie</FONT></h2>""",
    unsafe_allow_html=True,
)

# Symfony
for i in range(3):
    col[0].write("\n")
col[0].image("static/Illustrator.png", width=220)
col[0].write("\n")
col[0].write(
    """<p style="text-align: justify;"><B>Adobe Illustrator est 
    un logiciel de création graphique vectorielle utilisé pour 
    concevoir des illustrations, des logos, des infographies, 
    des icônes et bien d'autres types de visuels. Contrairement 
    aux images matricielles (comme celles créées avec Photoshop), 
    les graphiques vectoriels sont composés de formes géométriques et de courbes, 
    ce qui permet un redimensionnement sans perte de qualité.</B>
    </p>""",
    unsafe_allow_html=True,
)

# Photoshop
col[1].image("static/Photoshop.png", width=300)
col[1].write(
    """<p style="text-align: justify;"><B>Adobe Photoshop 
    est un logiciel de retouche photo et de création graphique 
    raster, utilisé principalement pour modifier, retoucher, 
    créer et manipuler des images. Il est largement utilisé 
    dans les domaines de la photographie, du design graphique, 
    de la création de contenu web, et bien plus encore.</B>
    </p>""",
    unsafe_allow_html=True,
)
