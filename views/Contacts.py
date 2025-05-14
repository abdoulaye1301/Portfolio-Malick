import streamlit as st
import requests
import re

WEBHOOK_URL = "https://connect.pabbly.com/workflow/sendwebhookdata/IjU3NjYwNTY4MDYzMDA0MzQ1MjY4NTUzZDUxMzQi_pc"


def valide_mail(email):
    email_pattern = r"^[a-zA-z0-9_.+-]+@[a-zA-z0-9-]+\.[a-zA-z0-9-.]+$"
    return re.match(email_pattern, email) is not None


def contact_form():
    with st.form("contact_form"):
        nom = st.text_input("Nom")
        prenom = st.text_input("Prénom")
        email = st.text_input("E-mail")
        message = st.text_area("Votre message")
        envoie = st.form_submit_button("Envoyer")

        if envoie:
            if not WEBHOOK_URL:
                st.error(
                    "Le mail de service ne fonctionne pas, veillez essayer plus tard",
                    icon="📧",
                )
                st.stop()
            if not nom:
                st.error("veillez entrer votre nom", icon="🧏‍♂️")
                st.stop()
            if not prenom:
                st.error("veillez entrer votre prénom", icon="🧏‍♂️")
                st.stop()
            if not email:
                st.error("veillez entrer votre adresse mail", icon="📧")
                st.stop()
            if not valide_mail(email):
                st.error("veillez entrer votre adresse mail valide", icon="📧")
                st.stop()
            if not message:
                st.error("veillez entrer votre message", icon="💼")
                st.stop()

            # donnees
            donnee = {"email": email, "nom": nom, "prenom": prenom, "message": message}
            reponse = requests.post(WEBHOOK_URL, json=donnee)

            if reponse.status_code == 200:
                st.success("Message envoyer avec succé")
            else:
                st.error("Erreur d'envoie du message.")


# st.markdown(
#   "<h1 style='text-align:center; bord-radius:10px; color:reed; font-size:24px;'>Formulaire de contact</h1>",
#  unsafe_allow_html=True,
# )
# formulaire = """
#    <form action="https://formsubmit.co/ndao1301@gmail.com" method="POST">
#       <input type="text" name="name" placeholder="NDAO" required>
#      <input type="text" name="name" placeholder="Moustapha" required>
#     <input type="email" name="email" placeholder="mbelbouck@gmail.com" required>
#    <button type="submit" class=button>Envoyer</button>
# </form>
# """


# st.markdown(formulaire, unsafe_allow_html=True)

# st.header("E-mail : ndao1301@gmail.com")
# st.header("Number : (+221) 77-694-89-72")"""
