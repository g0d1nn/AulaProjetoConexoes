import mysql.connector

# Função para conectar ao banco de dados MySQL
def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # Substitua pelo seu usuário
        password="",  # Substitua pela sua senha
        database="escola"  # Substitua pelo nome do seu banco de dados
    )
