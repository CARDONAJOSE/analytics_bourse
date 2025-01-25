import matplotlib.pyplot as plt
import streamlit as st

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
