import streamlit as st
import Controller.models.Cliente as Cliente  # Importar la clase Cliente
import Controller.clienteController as ClienteController  # Funciones de cliente
import os

def Registrar():
    idModificar = st.query_params.get_all("id")
    st.query_params.clear()
    clienteRecuperado = None
    if idModificar:
        # Si el parámetro no está vacío, significa que el usuario ha seleccionado para modificar
        idModificar = idModificar[0]  # idModificar = primer valor del array ID
        clienteRecuperado = ClienteController.SeleccionarPorID(idModificar)  # clienteRecuperado = cliente seleccionado para modificar
        st.query_params.id = [clienteRecuperado.id]  # Establecer el parámetro de modificación para el cliente a ser modificado
        st.title('Modificar registro :pencil2:')
    else:
        st.title('Registrar :white_check_mark:')

    with st.form(key='incluir_cliente'):
        listaTrabajos = ['Desarrollador Web', 'Diseñador', 'Ingeniero', 'DevOps', 'Estudiante', 'Analista']
        if clienteRecuperado is None:
            input_nombre = st.text_input(label='Ingrese el nombre del cliente:', placeholder='Nombre')
            input_edad = st.number_input(label='Ingrese la edad del cliente:', format='%i', step=1, min_value=18, max_value=120)
            input_trabajo = st.selectbox('Seleccione la profesión del cliente:', options=listaTrabajos)
            input_foto = st.file_uploader("Sube una foto del cliente", type=["jpg", "png"])
        else:
            input_nombre = st.text_input(label='Ingrese el nombre del cliente:', value=clienteRecuperado.nombre)
            input_edad = st.number_input(label='Ingrese la edad del cliente:', format='%i', step=1, min_value=18, max_value=120, value=clienteRecuperado.edad)
            input_trabajo = st.selectbox('Seleccione la profesión del cliente:', options=listaTrabajos, index=listaTrabajos.index(clienteRecuperado.profesion))
            input_foto = st.file_uploader("Sube una foto del cliente", type=["jpg", "png"])

        input_button_submit = st.form_submit_button("Enviar")

    if input_button_submit:
        foto_ruta = None
        if input_foto is not None:
            foto_ruta = os.path.join("fotos", input_foto.name)
            with open(foto_ruta, "wb") as f:
                f.write(input_foto.getbuffer())

        if clienteRecuperado is None:
            ClienteController.Incluir(Cliente.Cliente(0, input_nombre, input_edad, input_trabajo, foto_ruta))  # Función para incluir cliente en la base de datos
            st.success("¡Éxito! Cliente registrado.")
        else:
            st.query_params.clear()
            ClienteController.Modificar(Cliente.Cliente(clienteRecuperado.id, input_nombre, input_edad, input_trabajo, foto_ruta or clienteRecuperado.foto))  # Función para modificar cliente en la base de datos
            st.success("¡Éxito! Cliente modificado.")