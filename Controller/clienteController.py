from services import database as db
from Controller.models.Cliente import Cliente

def Incluir(cliente):
    db.cursor.execute(f'INSERT INTO clientes (nombreCliente, edadCliente, profesionCliente, fotoCliente) VALUES ("{cliente.nombre}", {cliente.edad}, "{cliente.profesion}", "{cliente.foto}")')
    db.bdConnection.commit()

def SeleccionarClientes():
    selectCommand = f'SELECT * FROM clientes'
    db.cursor.execute(selectCommand)
    listaClientes = []
    for row in db.cursor.fetchall():
        listaClientes.append(Cliente(row[0], row[1], row[2], row[3], row[4]))

    return listaClientes

def Eliminar(id):
    deleteCommand = f'DELETE FROM clientes WHERE idCliente = {id}'
    db.cursor.execute(deleteCommand)
    db.bdConnection.commit()

def Modificar(cliente):
    updateCommand = f'UPDATE clientes SET nombreCliente = "{cliente.nombre}", edadCliente = {cliente.edad}, profesionCliente = "{cliente.profesion}", fotoCliente = "{cliente.foto}" WHERE idCliente = {cliente.id}'
    db.cursor.execute(updateCommand)
    db.bdConnection.commit()

def SeleccionarPorID(id):
    selectId = f'SELECT * FROM clientes WHERE idCliente = {id}'
    db.cursor.execute(selectId)
    listaId = []
    for row in db.cursor.fetchall():
        listaId.append(Cliente(row[0], row[1], row[2], row[3], row[4]))

    return listaId[0]  # Retornando solo el valor necesario, que es el ID, de la columna 0 en la base de datos