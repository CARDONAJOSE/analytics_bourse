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


# Barre latérale
st.sidebar.title("Paramètres de personnalisation et de génération")

# Sélecteur de thème dans la barre latérale
theme = st.sidebar.selectbox(
    "Choisissez un thème :",
    ["Clair", "Sombre", "Vintage"]
)

# Appliquez le thème sélectionné
apply_theme(theme)

selected_moving_averages = st.selectbox(
    "Selecciona las medias móviles a visualizar:",
    options=["SMA 50", "SMA 100", "SMA 200", "Todas"],
    index=3,  # "Todas" seleccionada por defecto
)
plot_moving_averages(data, selected_moving_averages)

# Entradas del usuario
ticker = st.text_input("Introduit le ticker (exemple: AAPL):")
start_date = st.text_input("Insert la date de debut (format YYYY-MM-DD):")
end_date = st.text_input("Insert la date de fin (format YYYY-MM-DD):")

# Botón para validar la búsqueda
if st.button("Buscar"):
    if ticker and start_date and end_date:
        try:
            # Validar el formato de las fechas
            datetime.strptime(start_date, "%Y-%m-%d")
            datetime.strptime(end_date, "%Y-%m-%d")

            # Obtener los datos históricos
            data = yf.Ticker(ticker).history(start=start_date, end=end_date)
            st.session_state.data = data

            if data is not None and not data.empty:
                # Calcular estadísticas de volumen
                mean_volume = data['Volume'].mean()
                median_volume = data['Volume'].median()
                q75_volume = data['Volume'].quantile(0.75)

                # Mostrar estadísticas
                st.write(f"Volumen promedio: {mean_volume:.2f}")
                st.write(f"Mediana del volumen: {median_volume:.2f}")
                st.write(f"75º percentil del volumen: {q75_volume:.2f}")
                # graphique de volumen
                graph(mean_volume, median_volume, q75_volume, ticker)

            else:
                st.warning("No se encontraron datos para el ticker y rango de fechas especificado.")
        except ValueError:
            st.error("Formato de fecha incorrecto. Usa el formato YYYY-MM-DD.")
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Por favor, completa todos los campos.")
