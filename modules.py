import yfinance as yf
import matplotlib.pyplot as plt
import streamlit as st
def get_data(ticker, start_date, end_date):
    # recuperer les donnees de Yahoo Finance
    try:
        # Obtener los datos históricos
        data = yf.Ticker(ticker).history(start=start_date, end=end_date)
        return data
    except Exception as e:
        st.error(f"Error al obtener datos: {e}")
        return None

    

    
    