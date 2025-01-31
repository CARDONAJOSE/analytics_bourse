import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go



def plot_moving_averages(data, selected_moving_averages):
    """
    Graphique des medias mouvantes pour un ticker.

    Parámetros:
        data (pd.DataFrame): DataFrame con las columnas 'Date', 'Close', 'SMA_50', 'SMA_100', 'SMA_200'.
        selected_moving_averages (list): Lista de opciones seleccionadas.
    """
    # Verificar si los datos están disponibles
    if data is None or data.empty:
        st.warning("No hay datos disponibles para graficar.")
        return

    # Verificar si las columnas necesarias están presentes
    required_columns = ["Close", "SMA_8", "SMA_21", "SMA_50", "SMA_100", "SMA_200", "EMA_8", "EMA_21", "EMA_50", "EMA_100", "EMA_200"]
    if not all(col in data.columns for col in required_columns):
        st.error("Las columnas necesarias no están presentes en los datos.")
        return

    # Crear la gráfica
    plt.figure(figsize=(12, 6))
    
    # Graficar el precio de cierre
    plt.plot(data.index, data["Close"], label="Close", color="blue")
    
    # Graficar las medias móviles seleccionadas
    for ma in selected_moving_averages:
        if ma in data.columns:
            plt.plot(data.index, data[ma], label=ma)
    
    # Configuración de la gráfica
    plt.title("Ticket CAC - Medias Móviles")
    plt.xlabel("Date")
    plt.ylabel("Prix")
    plt.grid(True)
    plt.legend()
    
    # Mostrar la gráfica en Streamlit
    st.pyplot(plt)


def plot_buji_moving_averages(data, selected_moving_averages, ticker):
    """
    Graphique des medias mouvantes pour un ticker.

    Parámetros:
        data (pd.DataFrame): DataFrame con las columnas 'Date', 'Close', 'SMA_50', 'SMA_100', 'SMA_200'.
        selected_moving_averages (list): Lista de opciones seleccionadas.
    """
    # Verificar si los datos están disponibles
    if data is None or data.empty:
        st.warning("No hay datos disponibles para graficar.")
        return

    # Verificar si las columnas necesarias están presentes
    required_columns = ["Close", "SMA_8", "SMA_21", "SMA_50", "SMA_100", "SMA_200", "EMA_8", "EMA_21", "EMA_50", "EMA_100", "EMA_200"]
    if not all(col in data.columns for col in required_columns):
        st.error("Las columnas necesarias no están presentes en los datos.")
        return

    # Crear la gráfica
    fig = go.Figure()

    
    fig.add_trace(go.Candlestick(
    x=data.index,
    open=data['Open'],
    high=data['High'],
    low=data['Low'],
    close=data['Close'],
    name="Precio",
    ))
   
    # Graficar las medias móviles seleccionadas
    for ma in selected_moving_averages:
        if ma in data.columns:
            fig.add_trace(go.Scatter(
                x=data.index,
                y=data[ma],
                mode='lines',
                name=ma
            ))
    
   # Agregar títulos y etiquetas
    fig.update_layout(
    title={
            'text':f'Grapique de {ticker}',
            'x': 0.5,  # Centrar el título
            'xanchor': 'center'
            },
    xaxis_title='Date',
    yaxis_title='Prix',
    yaxis=dict(
            side='right'
        ),
    xaxis_rangeslider_visible=False,
    template="plotly_dark"
    )

# Mostrar en Streamlit
    st.plotly_chart(fig)