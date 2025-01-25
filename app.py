import yfinance as yf
import streamlit as st
from datetime import datetime
import matplotlib.pyplot as plt
import warnings
from modules.theme import apply_theme
from modules.graphique import graph
from modules.medias_movile import plot_moving_averages

# Ignorar advertencias
warnings.filterwarnings("ignore")

# Título de la aplicación
st.title("Analyses des données de bourse")

if "data" not in st.session_state:
    st.session_state.data = None

# Barre latérale
st.sidebar.title("Paramètres de personnalisation et de génération")

# Sélecteur de thème dans la barre latérale
theme = st.sidebar.selectbox(
    "Choisissez un thème :",
    ["Clair", "Sombre", "Vintage"]
)

# Appliquez le thème sélectionné
apply_theme(theme)

# Entradas del usuario en la barra lateral
st.sidebar.header("Paramètres de données")
ticker = st.sidebar.text_input("Introduit le ticker (exemple: AAPL):")
start_date = st.sidebar.text_input("Insert la date de debut (format YYYY-MM-DD):")
end_date = st.sidebar.text_input("Insert la date de fin (format YYYY-MM-DD):")

# Botón para validar la búsqueda
if st.sidebar.button("Buscar"):
    if ticker and start_date and end_date:
        try:
            # Validar el formato de las fechas
            datetime.strptime(start_date, "%Y-%m-%d")
            datetime.strptime(end_date, "%Y-%m-%d")

            # Obtener los datos históricos
            data = yf.Ticker(ticker).history(start=start_date, end=end_date)
            st.session_state.data = data  # Guardar los datos en session_state

            if data is not None and not data.empty:
                st.success("Données téléchargées avec succès!")
            else:
                st.warning("No se encontraron datos para le ticker et le range de dates spécifié.")
        except ValueError:
            st.error("Format de date incorrect. Utilisez le format YYYY-MM-DD.")
        except Exception as e:
            st.error(f"Erreur: {e}")
    else:
        st.warning("Veuillez remplir tous les champs.")

# Si los datos están disponibles, mostrar las gráficas
if "data" in st.session_state and st.session_state.data is not None:
    data = st.session_state.data

    # Mostrar estadísticas de volumen
    st.header("Statistiques de volume")
    mean_volume = data['Volume'].mean()
    median_volume = data['Volume'].median()
    q75_volume = data['Volume'].quantile(0.75)

    st.write(f"Volume moyen: {mean_volume:.2f}")
    st.write(f"Médiane du volume: {median_volume:.2f}")
    st.write(f"75e percentile du volume: {q75_volume:.2f}")

    # Gráfico de volumen
    st.header("Graphique de volume")
    graph(mean_volume, median_volume, q75_volume, ticker)

    # Gráfiques des moyeennes mobiles
    st.header("Graphique des moyennes mobiles")
    selected_moving_averages = st.selectbox(
        "Selecciona las medias móviles a visualizar:",
        options=["SMA 50", "SMA 100", "SMA 200", "Todas"],
        index=3,  # "Todas" seleccionada por defecto
    )
    plot_moving_averages(data, selected_moving_averages)