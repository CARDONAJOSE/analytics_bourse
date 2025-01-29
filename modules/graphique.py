import matplotlib.pyplot as plt
import streamlit as st
import calplot
import pandas as pd
import numpy as np

if "data" not in st.session_state:
    st.session_state.data = None
    
def graph(mean_volume, median_volume, q75_volume, ticker):
    try:
        data = st.session_state.data
        # Crear un gráfico
        fig, ax = plt.subplots()
        ax.plot(data.index, data['Volume'])
        ax.axhline(mean_volume, color='r', linestyle='--', label=f'Media: {mean_volume:.2f}')
        ax.axhline(median_volume, color='g', linestyle='-.', label=f'Mediana: {median_volume:.2f}')
        ax.axhline(q75_volume, color='b', linestyle=':', label=f'75º Percentil: {q75_volume:.2f}')
        ax.legend()
        ax.set_title(f"Estatisitiques de Volume pour {ticker}")
        st.pyplot(fig)
    except Exception as e:
        st.error(f"Erreur dans la graphique: {e}")


def plot_calendar(data):
    try:
        if not isinstance(data.index, pd.DatetimeIndex):
            
            raise ValueError("El índice de los datos no es un DatetimeIndex.")
        # Validar que no haya valores nulos o no válidos
        data.index = data.index.tz_localize(None)
        # Graficar usando el DataFrame con índice de fecha
        calplot.calplot(
            data['dif_jour'],
            cmap='Spectral_r',
            linewidth=1,
            suptitle='Calendrier',
            suptitle_kws={'x': 0.5, 'y': 1.0},
            daylabels=['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
        )
        st.pyplot(plt.gcf())
    except Exception as e:
        st.error(f"Error en la generación del gráfico: {e}")

