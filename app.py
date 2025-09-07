import streamlit as st
import pandas as pd
import plotly.express as px

# Título o encabezado
st.header('Análisis de Datos de Vehículos')

# Carga el dataset (ajusta la ruta si es necesario)
car_data = pd.read_csv("vehicles_us.csv")

# Botón para construir histograma
hist_button = st.button('Construir histograma')

if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x='odometer', title='Histograma de odómetro')
    st.plotly_chart(fig, use_container_width=True)

# Botón para construir gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos')
    fig2 = px.scatter(car_data, x='model_year', y='price', color='condition', title='Dispersión Precio vs Año')
    st.plotly_chart(fig2, use_container_width=True)
    

