import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv("vehicles_us.csv")
car_data["model_year"] = car_data["model_year"].astype("int", errors="ignore")

st.header("Construye tu gráfico")

hist_button = st.button("Construir histograma")

if hist_button:
    st.write("Odómetro de los vehículos disponibles")

    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig)


hist_check = st.checkbox("Marcar casilla para construir gráfico de dispersión")
if hist_check:
    fig = px.scatter(car_data, x="odometer", y="model_year")
    st.text("Odómetro de los vehículos por año")
    st.plotly_chart(fig)


st.subheader("¿Cuál es el vehículo más viejo")
model_check = st.checkbox("Haz click aquí para averiguarlo")
if model_check:
    st.dataframe(car_data[car_data["model_year"]
                 == car_data["model_year"].min()])
