import streamlit as st
import pandas as pd
import plotly.express as px

# Ler dados do arquivo CSV
df = pd.read_csv(r"C:\Users\Usuario\sprint_4\vehicles.csv")

# Exibir as primeiras linhas do dataframe
st.write("Preview dos dados:", df.head())

# Criar botão para gerar histograma
if st.button('Gerar Histograma'):
    fig_histogram = px.histogram(df, x="odometer")
    st.plotly_chart(fig_histogram)

# Criar botão para gerar gráfico de barras
if st.button('Gerar Gráfico de Barras'):
    fig_bar = px.bar(df, x='model_year', y='price', title='Preço por Ano do Modelo')
    st.plotly_chart(fig_bar)

# Criar botão para gerar gráfico de dispersão
if st.button('Gerar Gráfico de Dispersão'):
    fig_scatter = px.scatter(df, x='odometer', y='price', title='Preço vs. Quilometragem', color='condition')
    st.plotly_chart(fig_scatter)
