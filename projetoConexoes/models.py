import mysql.connector
from db import create_connection

# Classe Cliente (relacionada com Pedido em 1:N)
class Cliente:
    def __init__(self, id_cliente=None, nome=None):
        self.id_cliente = id_cliente
        self.nome = nome

    def save(self):
        conn = create_connection()
        cursor = conn.cursor()
        if self.id_cliente is None:  # Se não tiver ID, é um novo cliente (CREATE)
            cursor.execute("INSERT INTO clientes (nome) VALUES (%s)", (self.nome,))
        else:  # Se tiver ID, é uma atualização (UPDATE)
            cursor.execute("UPDATE clientes SET nome = %s WHERE id_cliente = %s", (self.nome, self.id_cliente))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM clientes")
        records = cursor.fetchall()
        conn.close()
        return [Cliente(id_cliente=row[0], nome=row[1]) for row in records]

    @staticmethod
    def delete(id_cliente):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM clientes WHERE id_cliente = %s", (id_cliente,))
        conn.commit()
        conn.close()


# Classe Pedido (relacionado com Cliente em 1:N)
class Pedido:
    def __init__(self, id_pedido=None, id_cliente=None, descricao=None):
        self.id_pedido = id_pedido
        self.id_cliente = id_cliente
        self.descricao = descricao

    def save(self):
        conn = create_connection()
        cursor = conn.cursor()
        if self.id_pedido is None:  # Novo pedido
            cursor.execute("INSERT INTO pedidos (id_cliente, descricao) VALUES (%s, %s)", 
                           (self.id_cliente, self.descricao))
        else:  # Atualização de pedido
            cursor.execute("UPDATE pedidos SET descricao = %s WHERE id_pedido = %s", 
                           (self.descricao, self.id_pedido))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM pedidos")
        records = cursor.fetchall()
        conn.close()
        return [Pedido(id_pedido=row[0], id_cliente=row[1], descricao=row[2]) for row in records]

    @staticmethod
    def delete(id_pedido):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM pedidos WHERE id_pedido = %s", (id_pedido,))
        conn.commit()
        conn.close()
