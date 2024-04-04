import streamlit as st
import pandas as pd
import os
import warnings
import yaml

with open("config.yaml", "r") as f:
                config = yaml.safe_load(f)

st.set_page_config(page_title= 'ListaProductos', page_icon= 'bar_chart:', layout='wide')
st.image("images/Blueberry.png", width=200)
st.title('Productos para el cuidado de arandanos')
st.markdown('<style>div.block-container{padding-top:1rem}</style>',unsafe_allow_html=True)
tabs = st.tabs([
    'Registrar producto', 'Predicciones', '... ', '...'
])



with tabs[0]:
    companies  = config['Empresas']
    st.multiselect("Selecciona una o más opciones:", companies, [])
