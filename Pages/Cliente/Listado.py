import streamlit as st
import Controller.clienteController as ClienteController
import Pages.Cliente.Registro as PageRegistro
import os

def Listado():
    paramId = st.query_params.get_all("id")
    if not paramId:  # Si el parámetro de modificación está vacío, lista normal de clientes.
        st.query_params.clear()
        st.title("Lista de clientes :clipboard:")

        # Ajustar el estilo del contenedor principal para ocupar todo el ancho
        st.markdown("""
        <style>
        .main-container {
            max-width: 100% !important;
        }
        .row {
            display: flex;
            justify-content: space-between;
            width: 100%;
            margin-bottom: 1rem;
        }
        .column {
            flex: 1;
            padding: 0 0.5rem;
            text-align: center;
        }
        .actions {
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column; /* Alinear los botones en columna */
            gap: 0.5rem; /* Ajustar el espacio entre botones */
        }
        </style>
        """, unsafe_allow_html=True)

        # Usar un container para envolver el contenido
        with st.container():
            columnas = st.columns((1, 1, 2, 1, 2, 2))  # Ajustar tamaños de las columnas
            atributos = [':file_folder: ID', ':frame_with_picture: Foto', ':page_facing_up: Nombre', ':calendar: Edad', ':construction_worker: Profesión', ':x: Eliminar / :arrows_clockwise: Modificar']
            for columna, nombre_atributo in zip(columnas, atributos):
                columna.write(nombre_atributo)

            for x, item in enumerate(ClienteController.SeleccionarClientes()):
                columnas = st.columns((1, 1, 2, 1, 2, 2))  # Ajustar tamaños de las columnas
                columnas[0].write((str(item.id)))

                # Mostrar la foto si existe
                with columnas[1]:
                    if item.foto and os.path.exists(item.foto):
                        st.image(item.foto, width=100)  # Ajustar el tamaño de la imagen
                    else:
                        st.write("No hay foto")

                columnas[2].write(item.nombre)
                columnas[3].write(str(item.edad))
                columnas[4].write(item.profesion)

                # Ajustar la alineación de los botones
                with columnas[5]:
                    st.markdown('<div class="actions">', unsafe_allow_html=True)
                    if st.button('Eliminar', key=f'eliminar_{item.id}'):
                        ClienteController.Eliminar(item.id)
                        st.experimental_rerun()  # Recarga la página para que el cliente desaparezca de la lista
                    if st.button('Modificar', key=f'modificar_{item.id}'):
                        st.query_params.id = [item.id]  # Establecer el parámetro ID en la URL para obtener en la página de registro
                        st.experimental_rerun()  # Recarga para garantizar
                    st.markdown('</div>', unsafe_allow_html=True)
    else:
        PageRegistro.Registrar()  # Registro en modo 'Modificar' porque el parámetro ID no está vacío.
        clickBack = st.button('Volver')
        if clickBack:
            st.query_params.clear()  # Limpiar el parámetro para liberar de la pantalla de modificación
            st.experimental_rerun()  # Recarga