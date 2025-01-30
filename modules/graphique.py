import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

import streamlit as st
import calplot
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.io as pio

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
            cmap='RdYlGn',
            vmin=-2, vmax=2,
            linewidth=1,
            suptitle='Calendrier',
            suptitle_kws={'x': 0.5, 'y': 1.0, 'ha': 'center'},
            daylabels=['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
        )
        st.pyplot(plt.gcf())
    except Exception as e:
        st.error(f"Error en la generación del gráfico: {e}")

def graphique_volumen(data, ticker):

    try:
        vol_media = data['Volume'].mean()


        # Determinar el color de las barras: verde si el cierre sube, rojo si baja
        colors = ['green' if close_today > close_yesterday else 'red' 
          for close_today, close_yesterday in zip(data['Close'], data['Close'].shift(1))]

        # Crear gráfico de volumen con colores personalizados
        fig = go.Figure()

        # Agregar barras de volumen
        fig.add_trace(go.Bar(
        x=data.index, 
        y=data['Volume'], 
        name='Volume',
        marker_color=colors,  # Asignar colores rojo/verde
        opacity=0.6
        ))

        # Agregar línea de media móvil de volumen
        fig.add_trace(go.Scatter(
        x=data.index, 
        y=[vol_media]*len(data), 
        mode='lines', 
        name='Moyenne', 
        line=dict(color='black', width=2)
        ))

        # Configurar diseño del gráfico
        fig.update_layout(
        title=f'Volumen de transactions {ticker}',
        xaxis_title='date',
        yaxis_title='Volumen',
        template="plotly_dark",
        xaxis=dict(
        rangeslider=dict(visible=True),  
        type="date"
        ),
        legend=dict(x=0, y=1)
        )

        # Mostrar gráfico
        st.plotly_chart(fig)
    except Exception as e:
        st.error(f"Erreur dans la graphique: {e}")