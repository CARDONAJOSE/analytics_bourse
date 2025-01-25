import streamlit as st

# Fonction pour appliquer les thèmes
def apply_theme(theme: str):
    """
    Applique un thème visuel en injectant du CSS en utilisant les classes spécifiques identifiées dans l'application.
    """
    if theme == "Clair":
        st.markdown(
            """
            <style>
            body {
                background-color: #FFFFFF;
                color: #000000;
            }
            .stSidebar {
                background-color: #F0F2F6;
            }
            .stButton > button {
                background-color: #007BFF;
                color: #FFFFFF;
                border-radius: 5px;
            }
            .stButton > button:hover .st {
                background-color: #005A9E;
            }
            /* Styles pour les titres */
            .st-emotion-cache-1espb9k h1, .st-emotion-cache-1espb9k h2, .st-emotion-cache-1espb9k h3 {
                color: #333333;
                font-weight: bold;
            }
            /* Styles pour les paragraphes */
            .st-emotion-cache-14553y9 p, .st-emotion-cache-1cvow4s p, st-emotion-cache-1qrd9al e121c1cl0 p, .st-emotion-cache-1qrd9al p, .st-emotion-cache-1vsah7k p {
                color: #555555;
            }
            /* Exclure le texte du bouton */
            button .st-emotion-cache-1vsah7k p {
                color: #FFFFFF !important;
            }
            textarea, select {
                background-color: #FFFFFF;
                color: #000000;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
    elif theme == "Sombre":
        st.markdown(
            """
            <style>
            body {
                background-color: #121212;
                color: #FFFFFF;
            }
            .stSidebar {
                background-color: #333333;
            }
            .stButton > button {
                background-color: #007BFF;
                color: #FFFFFF;
                border-radius: 5px;
            }
            /* Styles pour les titres */
            .st-emotion-cache-1espb9k h1, .st-emotion-cache-1espb9k h2, .st-emotion-cache-1espb9k h3 {
                color: #FFFFFF;
                font-weight: bold;
            }
            /* Styles pour les paragraphes */
            .st-emotion-cache-14553y9 p {
                color: #CCCCCC;
            }
            textarea, select {
                background-color: #1E1E1E;
                color: #FFFFFF;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
    elif theme == "Vintage":
        st.markdown(
            """
            <style>
            body {
                background-color: #FAEBD7;
                color: #5A4632;
                font-family: 'Courier New', Courier, monospace;
            }
            .stSidebar {
                background-color: #FFE4C4;
            }
            .stButton > button {
                background-color: #8B4513;
                color: #FFFFFF;
                border-radius: 5px;
            }
            /* Styles pour les titres */
            .st-emotion-cache-1espb9k h1, .st-emotion-cache-1espb9k h2, .st-emotion-cache-1espb9k h3 {
                color: #8B4513;
                font-weight: bold;
            }
            /* Styles pour les paragraphes */
            .st-emotion-cache-14553y9 p, .st-emotion-cache-1qrd9al p, .st-emotion-cache-1vsah7k p {
                color: #5A4632;
            }
            /* Exclure le texte du bouton */
            button .st-emotion-cache-1vsah7k p {
                color: #FFFFFF !important;
            }
            textarea, select {
                background-color: #FFF8DC;
                color: #5A4632;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
