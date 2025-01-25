import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd


data = st.session_state.data

# Función para graficar las medias móviles
def plot_moving_averages(data, selected_moving_averages):
    """
    Graphique des medias mouvantes pour un ticker

    Parámetros:
        data (pd.DataFrame): DataFrame con las columnas 'Date', 'Close', 'SMA_50', 'SMA_100', 'SMA_200'.
        selected_moving_averages (str): Opción seleccionada en el selectbox.
    """
    
    plt.figure(figsize=(12, 6))
    
    # Graficar el precio de cierre
    plt.plot(data.index, data["Close"], label="Close", color="blue")
    
    # Graficar las medias móviles seleccionadas
    if selected_moving_averages == "SMA 50" or selected_moving_averages == "Todas":
        plt.plot(data.index, data["SMA_50"], label="SMA 50", color="orange")
    if selected_moving_averages == "SMA 100" or selected_moving_averages == "Todas":
        plt.plot(data.index, data["SMA_100"], label="SMA 100", color="green")
    if selected_moving_averages == "SMA 200" or selected_moving_averages == "Todas":
        plt.plot(data.index, data["SMA_200"], label="SMA 200", color="red")
    
    # Configuración de la gráfica
    plt.title("ticket CAC 40 - Medias Móviles")
    plt.xlabel("date")
    plt.ylabel("Prix")
    plt.grid(True)
    plt.legend()
    
    # Mostrar la gráfica en Streamlit
    st.pyplot(plt)



