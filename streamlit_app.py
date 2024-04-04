import streamlit as st
import pandas as pd
import os
import warnings
import yaml



st.set_page_config(page_title= 'ListaProductos', page_icon= 'bar_chart:', layout='wide')
st.image("images/Blueberry.png", width=200)
st.title('Productos para el cuidado de arandanos')
st.markdown('<style>div.block-container{padding-top:1rem}</style>',unsafe_allow_html=True)
tabs = st.tabs([
    'Registrar producto', 'Predicciones', '... ', '...'
])



with tabs[0]:
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)
    col1, col2, col3 = st.columns(3)
    with col1:
        companies  = config['Empresas']
        selection = st.selectbox("Selecciona la marca del producto", companies)
    with col2:
        clasificacion  = config['Clasificacion']
        clasif = st.multiselect("Selecciona clasificacion del producto", clasificacion, [])
    with col3:
        nombreComercial = st.text_input("Nombre comercial")
    col4, col5, col6 = st.columns(3)
    with col4:
        modoAccion  = config['modoAccion']
        modo_accion = st.multiselect("Selecciona clasificacion del producto", modoAccion, [])
    with col5:
        modoAplicacion  = config['modoAplicacion']
        modo_aplicacion = st.multiselect("Selecciona clasificacion del producto", modoAplicacion, [])
    with col6:
        etiqueta  = config['etiqueta']
        etiqueta_select = st.selectbox("Selecciona clasificacion del producto", etiqueta)
    col7, col8, col9 = st.columns(3)
    with col7:
        control  = config['control']
        problemas_controla = st.multiselect("Selecciona la problema que controla el producto", control, [])
    with col8:
        favorece  = config['favorece']
        favorece_ = st.multiselect("Selecciona lo que favorece  el producto", favorece, [])
    #subir archivo
    archivo = st.file_uploader("Agrega la fuicha tecnica", type=['pdf'])
    if archivo is not None:
        st.write("Nombre del archivo: ",archivo.name)
        if st.button("Guardar archivo"):
            if not os.path.exists(selection):
                os.makedirs(selection)
            # st.write(type(selection))
            # st.write( type(archivo.name))
            print(type(selection))
            print(type(archivo.name))

            ruta_archivo = os.path.join(selection, archivo.name)
            # with open(ruta_archivo, "wb") as f:
            #     f.write(archivo.getbuffer())
            st.success("Archivo guardado exitosamente")

            product_list = config['productosRegistrados']
            id_product = len(product_list) + 1
            config['productosRegistrados'].append(ruta_archivo)
            with open("config.yaml", "w") as archivo:
                config = yaml.dump(config ,archivo, default_flow_style=False)

            record = {
                "idProducto": id_product,
                "clasificacion": clasif,
                "nombreComercial": nombreComercial,
                "ingredienteActivo": "Captan",
                "pIA": 50,
                "fracIrac": "M04",
                "modoAccion": modo_accion,
                "control": problemas_controla,
                "favorece":  favorece_,
                "modoAplicacion": modo_aplicacion,
                "diasProteccion": "12-14 días",
                "etiqueta": etiqueta_select,
                "marca": selection,
                "ubicacion": ruta_archivo
            }
            st.json(record)