import streamlit as st

# from st_pages import add_page_title, hide_pages

# add_page_title()

# hide_pages(["Thank you"])

st.warning("#### Report a bug 👾 or request a feature ⚡")

st.markdown("#### 📬 Get In Touch With Me!")

contact_form = """
<form action="https://formsubmit.co/ndao1301@gmail.com" method="POST" enctype="multipart/form-data">
    <input type="text" name="Nom" placeholder="Votre nom complet" required>
    <input type="text" name="Objet" placeholder="Objet" required>
    <input type="email" name="Email" placeholder="Votre adresse mail" required>
     <textarea name="Message" placeholder="Votre message"></textarea>
     <br>
     <input type="hidden" name="_next" value="https://monportfolio-nd.streamlit.app/">
     <button type="submit">Envoyer</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)


hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""


# Use Local CSS File
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style.css")

st.markdown(hide_streamlit_style, unsafe_allow_html=True)
