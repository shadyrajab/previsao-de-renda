import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(
     page_title="Previsão de Renda?",
     page_icon="💵",
     layout="wide",
)

st.write('# Análise exploratória da previsão de renda')

renda = pd.read_csv('./input/previsao_de_renda.csv')

with st.container(border = True):
    df = renda[['posse_de_imovel', 'renda']]
    fig = px.histogram(df, x='posse_de_imovel')

    st.plotly_chart(fig, theme='streamlit', use_container_width=True)

st.write('## Gráficos ao longo do tempo')

with st.container(border = True):
    df = renda.groupby(['posse_de_imovel', 'data_ref'], as_index=False).mean(numeric_only=True)
    fig = px.line(df, x='data_ref', y='renda', color='posse_de_imovel')

    st.plotly_chart(fig, theme='streamlit', use_container_width=True)

with st.container(border = True):
    df = renda.groupby(['posse_de_veiculo', 'data_ref'], as_index=False).mean(numeric_only=True)
    fig = px.line(df, x='data_ref', y='renda', color='posse_de_veiculo')

    st.plotly_chart(fig, theme='streamlit', use_container_width=True)

with st.container(border = True):
    df = renda.groupby(['qtd_filhos', 'data_ref'], as_index=False).mean(numeric_only=True)
    fig = px.line(df, x='data_ref', y='renda', color='qtd_filhos')

    st.plotly_chart(fig, theme='streamlit', use_container_width=True)

with st.container(border = True):
    df = renda.groupby(['tipo_renda', 'data_ref'], as_index=False).mean(numeric_only=True)
    fig = px.line(df, x='data_ref', y='renda', color='tipo_renda')

    st.plotly_chart(fig, theme='streamlit', use_container_width=True)

with st.container(border = True):
    df = renda.groupby(['educacao', 'data_ref'], as_index=False).mean(numeric_only=True)
    fig = px.line(df, x='data_ref', y='renda', color='educacao')

    st.plotly_chart(fig, theme='streamlit', use_container_width=True)

with st.container(border = True):
    df = renda.groupby(['estado_civil', 'data_ref'], as_index=False).mean(numeric_only=True)
    fig = px.line(df, x='data_ref', y='renda', color='estado_civil')

    st.plotly_chart(fig, theme='streamlit', use_container_width=True)

with st.container(border = True):
    df = renda.groupby(['tipo_residencia', 'data_ref'], as_index=False).mean(numeric_only=True)
    fig = px.line(df, x='data_ref', y='renda', color='tipo_residencia')

    st.plotly_chart(fig, theme='streamlit', use_container_width=True)

st.write('## Gráficos bivariada')

with st.container(border = True):
    fig = px.bar(renda, x='posse_de_imovel', y='renda')

    st.plotly_chart(fig, theme='streamlit', use_container_width=True)

with st.container(border = True):
    fig = px.bar(renda, x='posse_de_veiculo', y='renda')

    st.plotly_chart(fig, theme='streamlit', use_container_width=True)

with st.container(border = True):
    fig = px.bar(renda, x='qtd_filhos', y='renda')

    st.plotly_chart(fig, theme='streamlit', use_container_width=True)

with st.container(border = True):
    fig = px.bar(renda, x='tipo_renda', y='renda')

    st.plotly_chart(fig, theme='streamlit', use_container_width=True)

with st.container(border = True):
    fig = px.bar(renda, x='educacao', y='renda')

    st.plotly_chart(fig, theme='streamlit', use_container_width=True)

with st.container(border = True):
    fig = px.bar(renda, x='estado_civil', y='renda')

    st.plotly_chart(fig, theme='streamlit', use_container_width=True)

with st.container(border = True):
    fig = px.bar(renda, x='tipo_residencia', y='renda')

    st.plotly_chart(fig, theme='streamlit', use_container_width=True)


