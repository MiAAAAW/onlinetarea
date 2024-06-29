import mysql.connector
from os import environ

HOST = environ.get('HOST', 'localhost')
PASSWD = environ.get('PASSWD', '')
USER = environ.get('USER', 'root')
DATABASE = environ.get('DATABASE', 'tarea')

bdConnection = mysql.connector.connect(
    host=f'{HOST}',
    user=f'{USER}',
    password=f'{PASSWD}',
    database=f'{DATABASE}',
)  # Conexão com dados do banco de dados e MySQL

cursor = bdConnection.cursor()  # Cursor para executar conexão
bdConnection.commit()