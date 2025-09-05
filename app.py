import streamlit as st
import pandas as pd

# Importar librerías
import plotly.express as px

# Título de la aplicación
st.header("Dashboard de Anuncios de Coches")

# Cargar dataset
car_data = pd.read_csv('vehicles_us.csv')

# Mostrar un mensaje
st.write("Bienvenido a la aplicación web de análisis de vehículos.")

# Botón para crear histograma
hist_button = st.button('Construir histograma')

if hist_button:
    st.write('Creando histograma de odómetro...')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)
    st.write('Histograma creado con éxito.')
    st.balloons()

# Botón para scatter plot
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    st.write('Creando gráfico de dispersión: Precio vs Odómetro...')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)

    
