import matplotlib.pyplot as plt
import streamlit as st
import calplot
import pandas as pd
import numpy as np
import plotly.graph_objects as go

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


def plot_calendar(data, ticker, vmin=-4, vmax=4):
    try:
        if not isinstance(data.index, pd.DatetimeIndex ):
            
            raise ValueError("El índice de los datos no es un DatetimeIndex.")
        # Validar que no haya valores nulos o no válidos
        data.index = data.index.tz_localize(None)
        
        data['dif_jour'] = pd.to_numeric(data['dif_jour'], errors='coerce')

        # Graficar usando el DataFrame con índice de fecha
        calplot.calplot(
            data['dif_jour'],
            cmap='RdYlGn',
            vmin= vmin, 
            vmax= vmax,
            linewidth=1,
            suptitle=f'Calendrier de {ticker}',
            suptitle_kws={'x': 0.5, 'y': 1.05, 'ha': 'center'},
            daylabels=['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
        )
        st.pyplot(plt.gcf())
    except Exception as e:
        st.error(f"Erreur dans la graphique: {e}")

def graphique_volumen(data, ticker):

    try:
        #calculer la moyenne de volume
        vol_media = data['Volume'].mean()

        st.write(f"**Volatilité moyenne:** {vol_media:.2f}")

        # determine la coleur de la barre: vert si le prix augmente, rouge si baisse
        colors = ['green' if close_today > close_yesterday else 'red' 
          for close_today, close_yesterday in zip(data['Close'], data['Close'].shift(1))]

        #creer le graphique du volume 
        fig = go.Figure()

        #ajouter la barre de volume
        fig.add_trace(go.Bar(
        x=data.index, 
        y=data['Volume'], 
        name='Volume',
        marker_color=colors, 
        opacity=1
        ))

        # ajoute linea de media mobile
        fig.add_trace(go.Scatter(
        x=data.index, 
        y=[vol_media]*len(data), 
        mode='lines', 
        name='Moyenne', 
        line=dict(color='black', width=1)
        ))

        # Configurer la graphique
        fig.update_layout(
        title={
            'text':f'Volume des transactions {ticker}',
            'x': 0.5,  # Centrar el título
            'xanchor': 'center'},
        xaxis_title='Date',
        yaxis_title='Volume',
        yaxis=dict(
            side='right'
        ),
        template="ggplot2",
        xaxis=dict(
        rangeslider=dict(visible=True),  
        type="date"
        ),
        legend=dict(x=0, y=1)
        )

        # Mostrer gráphique
        st.plotly_chart(fig)
    except Exception as e:
        st.error(f"Erreur dans la graphique: {e}")


# Calcular la volatilidad
def plot_volatilite(data, ticker):

    try:
        # Mostrar la volatilidad media
        st.write(f"**Volatilité moyenne:** {data['Volatilité'].mean():.2f}")

        # Crear un gráfico de línea con plotly
        fig = go.Figure()

        # Agregar la línea de volatilidad
        fig.add_trace(go.Scatter(
        x=data.index,
        y=data["Volatilité"],
        mode='lines',
        name='Volatilité'
        ))
        fig.add_trace(go.Scatter(
        x=data.index, 
        y=[data['Volatilité'].mean()]*len(data), 
        mode='lines', 
        name='Moyenne', 
        line=dict(color='black', width=1)
        ))

    # Configurar el diseño del gráfico
        fig.update_layout(
            title={
            'text':f'Volatilité de {ticker}',
            'x': 0.5,  # Centrar el título
            'xanchor': 'center'},
            xaxis_title='Date',
            yaxis_title='Volatilité',
            yaxis=dict(
            side='right'  # Mover el eje y al lado derecho
            ),
            template="ggplot2"
        )
    except Exception as e:
        st.error(f"Erreur dans la graphique: {e}")

# Mostrar el gráfico en Streamlit
    st.plotly_chart(fig)