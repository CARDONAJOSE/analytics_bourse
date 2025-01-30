import yfinance as yf
import streamlit as st
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import warnings
from modules.theme import apply_theme
from modules.graphique import graph, plot_calendar, graphique_volumen
from modules.medias_movile import plot_moving_averages, plot_buji_moving_averages
import mplfinance as mpf
import plotly.graph_objects as go



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
frequency = st.sidebar.selectbox("Frequênce", ["1d", "5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y"])
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
            data = yf.Ticker(ticker).history(start=start_date, end=end_date, interval=frequency)
            st.session_state.data = data  # Guardar los datos en session_state
            
            if data is not None and not data.empty:
                st.success("Données téléchargées avec succès!")
            else:
                st.warning("No se encontraron datos pour le ticker et le range de dates spécifié.")
        except ValueError:
            st.error("Format de date incorrect. Utilisez le format YYYY-MM-DD.")
        except Exception as e:
            st.error(f"Erreur: {e}")
    else:
        st.warning("Veuillez remplir tous les champs.")

# Si los datos están disponibles, mostrar las gráficas
if "data" in st.session_state and st.session_state.data is not None:
    data = st.session_state.data

    # calculer la fiference de prix par jour
    data['dif_jour'] = data['Open'] - data['Close']
    
    # montre le statistique de prix
    st.header("📊 Statistiques des Prix et du Volume")

    st.write(f"**Prix d'ouverture moyen:** {data['Open'].mean():.2f}")
    st.write(f"**Prix de clôture moyen:** {data['Close'].mean():.2f}")
    st.write(f"**Prix le plus haut moyen:** {data['High'].mean():.2f}")
    st.write(f"**Prix le plus bas moyen:** {data['Low'].mean():.2f}")
    st.write(f"**Volume moyen des transactions:** {data['Volume'].mean():,.0f}")


    ## medias mobiles simple
    data["SMA_50"] = data["Close"].rolling(window=50).mean()
    data["SMA_8"] = data["Close"].rolling(window=8).mean()
    data["SMA_21"] = data["Close"].rolling(window=21).mean()
    data["SMA_100"] = data["Close"].rolling(window=100).mean()
    data["SMA_200"] = data["Close"].rolling(window=200).mean()

    # medias mobiles exponenciel
    data["EMA_8"] = data["Close"].ewm(span=8, adjust=False).mean()
    data["EMA_21"] = data["Close"].ewm(span=21, adjust=False).mean()
    data["EMA_50"] = data["Close"].ewm(span=50, adjust=False).mean()
    data["EMA_100"] = data["Close"].ewm(span=100, adjust=False).mean()
    data["EMA_200"] = data["Close"].ewm(span=200, adjust=False).mean()

    st.header("📉 Graphique de volatilité")
    data["Volatilité"] = data["High"] - data["Low"]
    st.write(f"**Volatilité moyenne:** {data['Volatilité'].mean():.2f}")
    st.line_chart(data["Volatilité"])


    st.dataframe(data)

    # Gráphique de volumen
    st.header("Graphique de volume")
    
    graphique_volumen(data, ticker)

    # Gráfiques des moyeennes mobiles
    st.header("Graphique des moyennes mobiles")

    # Seleccioner les moyennes móbiles
    col1, col2 = st.columns(2, vertical_alignment="bottom")
    with col1:
        st.subheader("Moyennes mobiles simples")
        sma_8=st.checkbox("SMA_8")
        sma_21=st.checkbox("SMA_21")
        sma_50=st.checkbox("SMA_50")
        sma_100=st.checkbox("SMA_100")
        sma_200=st.checkbox("SMA_200")
    with col2:
        st.subheader("Moyennes mobiles expon")
        ema_8= st.checkbox("EMA_8")        
        ema_21= st.checkbox("EMA_21")
        ema_50= st.checkbox("EMA_50")
        ema_100= st.checkbox("EMA_100")
        ema_200= st.checkbox("EMA_200")

    selected_moving_averages = []

    # Agregar las medias móviles seleccionadas a la lista
    if sma_8:
        selected_moving_averages.append("SMA_8")
    if sma_21:
        selected_moving_averages.append("SMA_21")
    if sma_50:
        selected_moving_averages.append("SMA_50")
    if sma_100:
        selected_moving_averages.append("SMA_100")
    if sma_200:
        selected_moving_averages.append("SMA_200")
    if ema_8:
        selected_moving_averages.append("EMA_8")
    if ema_21:
        selected_moving_averages.append("EMA_21")
    if ema_50:
        selected_moving_averages.append("EMA_50")
    if ema_100:
        selected_moving_averages.append("EMA_100")
    if ema_200:
        selected_moving_averages.append("EMA_200")
    #graphique des moyennes mobiles
    plot_buji_moving_averages(data, selected_moving_averages, ticker)

    # plot_moving_averages(data, selected_moving_averages)

    # Ajustes previos a las funciones
    st.header("Graphique de calendrier")     
    st.write("graphique de calendrier qui representa de jour positif ou negative dans un periode de temps")  # Mostrar tabla
    plot_calendar(data)  # Graphique le calendrier










