import streamlit as st
import Pages.Cliente.Registro as PageRegistro
import Pages.Cliente.Listado as PageListado

# Aplicar estilos CSS para ajustar el ancho
st.markdown("""
    <style>
        .stApp {
            max-width: 100% !important;
            padding: 2rem !important;
        }
    </style>
""", unsafe_allow_html=True)

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.title('Sistema de clientes :busts_in_silhouette:')
st.sidebar.title(':page_facing_up: Menú')
opciones_sidebar = st.sidebar.selectbox('Cliente', ['Registro', 'Consultar/Modificar'])

if opciones_sidebar == 'Registro':
    st.query_params.clear()
    PageRegistro.Registrar()

if opciones_sidebar == 'Consultar/Modificar':
    PageListado.Listado()
