import streamlit as st
import pandas as pd
import plotly.express as px
car_data=pd.read_csv("vehicles_us.csv")
st.header("Construir un histograma")
hist_button=st.button("Construir histograma")
if hist_button:
    st.write("El histograma se está construyedo")

    fig=px.histogram(car_data,x="odometer")

    st.plotly_chart(fig)
