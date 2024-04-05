import streamlit as st
import pandas as pd
import os
import warnings
import yaml
from dotenv import load_dotenv
from func import *
import pandas as pd
import plotly.express as px

load_dotenv('venv/.env')
connection_url = os.getenv('connection_url')
collecction_producto = os.getenv('collecction_producto')
db_ecoterra = remitente = os.getenv('db_ecoterra')

collection_products = coneccionDB(mongo_uri=connection_url, database_name=db_ecoterra, collection_name=collecction_producto)
total = collection_products.count_documents({}) 
# st.write("total de registros existentes", total)

st.set_page_config(page_title= 'ListaProductos', page_icon= 'bar_chart:', layout='wide')
st.image("images/Blueberry.png", width=200)
st.title('Productos para el cuidado de arandanos')
st.markdown('<style>div.block-container{padding-top:1rem}</style>',unsafe_allow_html=True)
tabs = st.tabs([
    'Registrar producto', 'Ver productos', '... ', '...'
])



with tabs[0]:
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)
    col1, col2, col3 = st.columns(3)
    with col1:
        companies  = config['Empresas']
        selection = st.selectbox("Selecciona clasificacion del producto", companies)
        if selection in ['Agregar']:
            selection = st.text_input("Ingrese un nuevo nombre")
            if st.button('Confirmar'):
                st.write("Nueva empresa registrada", selection)
                config_editado = config
                config_editado['Empresas'].append(selection)
                with open('config.yaml', 'w') as config_editado:
                    yaml.dump(config, config_editado)
        else:
            st.write("Empresa registrada", selection)
    with col2:
        clasificacion  = config['Clasificacion']
        clasif = st.multiselect("Selecciona clasificacion del producto", clasificacion, [])
    with col3:
        nombreComercial = st.text_input("Nombre comercial")
    col4, col5, col6 = st.columns(3)
    with col4:
        modoAccion  = config['modoAccion']
        modo_accion = st.multiselect("Clasificacion del producto", modoAccion, [])
    with col5:
        modoAplicacion  = config['modoAplicacion']
        modo_aplicacion = st.multiselect("Modo de aplicacion del producto", modoAplicacion, [])
    with col6:
        etiqueta  = config['etiqueta']
        etiqueta_select = st.selectbox("Color de etiqueta", etiqueta)
    col7, col8, col9 = st.columns(3)
    with col7:
        control  = config['control']
        problemas_controla = st.multiselect("Problema que controla el producto", control, [])
        if problemas_controla in ['Agregar']:
            problemas_controla = st.text_input("Ingrese un nuevo tipo de incidente")
            if st.button('Confirmar'):
                st.write("Nueva problematica registrada", selection)
                config['control'].append(selection)
                with open('config.yaml', 'w') as config_orig:
                    yaml.dump(config_orig, config)
    with col8:
        favorece  = config['favorece']
        favorece_ = st.multiselect("Selecciona lo que favorece  el producto", favorece, [])

    col10, col11, col12 = st.columns(3)
    with col10:
        ingrediente_activo = st.text_input("Ingrediente activo")
    with col11:
        Porc_ingrediente_activo = st.slider(" % de ingrdiente activo", 0, 100)
    #subir archivo  


    
    archivo = st.file_uploader("Agrega la ficha técnica", type=['pdf'])
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

            # product_list = config['productosRegistrados']
            id_product = total + 1
            config['productosRegistrados'].append(ruta_archivo)
            with open("config.yaml", "w") as archivo:
                config = yaml.dump(config ,archivo, default_flow_style=False)

            record = {
                "idProducto": id_product,
                "clasificacion": clasif,
                "nombreComercial": nombreComercial,
                "ingredienteActivo": ingrediente_activo,
                "pIA": Porc_ingrediente_activo,
                "modoAccion": modo_accion,
                "control": problemas_controla,
                "favorece":  favorece_,
                "modoAplicacion": modo_aplicacion,
                "etiqueta": etiqueta_select,
                "marca": selection,
                "ubicacion": ruta_archivo
            }
            st.json(record)
            collection_products.insert_one(record)

with tabs[1]:
    None
    # st.title("Productos Registrados")
    collection_products = coneccionDB(mongo_uri=connection_url, database_name=db_ecoterra, collection_name=collecction_producto)
    data = list(collection_products.find())
    df = pd.DataFrame(data=data)
    col_editablesss = ['clasificacion', 'nombreComercial','ingredienteActivo', 'pIA', 'etiqueta', 'marca']
    df =  df[col_editablesss]
    df_editable = df.copy()

    editable_df = st.data_editor(df_editable)


    # tabla_editable = st.table(df_editable)

    # if st.button("Guardar cambios"):
    #     edited_data = tabla_editable.data
    #     for idx, row in enumerate(edited_data):
    #         collection_products.update_one({'_id':row['_id']}, {'$set':row}, upsert=False)
    #     st.success("Editado de manera exitosa")