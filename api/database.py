import sqlite3
import pathlib
from typing import List, Dict

DATABASE = pathlib.Path(__file__).parent / 'database.sqlite'

class DatabaseAPI:
    def __init__(self):
        self.connection = sqlite3.connect(DATABASE)
        self.connection.row_factory = sqlite3.Row

    def close_connection(self):
        self.connection.close()

    def get_categorias(self) -> List[Dict]:
        cursor = self.connection.cursor()
        result = cursor.execute('SELECT * FROM categoria').fetchall()
        self.close_connection()
        return [dict(row) for row in result]
    
    def get_estoques(self) -> List[Dict]:
        cursor = self.connection.cursor()
        result = cursor.execute('SELECT * FROM estoque').fetchall()
        self.close_connection()
        return [dict(row) for row in result]
    
    def get_produtos(self, id_estoque: int) -> List[Dict]:
        cursor = self.connection.cursor()
        result = cursor.execute('SELECT * FROM produto WHERE id_estoque = ?', (id_estoque,)).fetchall()
        self.close_connection()
        return [dict(row) for row in result]
    
    def create_estoque(self, data: str) -> int:
        cursor = self.connection.cursor()
        estoque_id = cursor.execute('INSERT INTO estoque (data) VALUES (?)', (data,)).lastrowid
        self.connection.commit()
        self.close_connection()
        return estoque_id
    
    def create_categoria(self, nome: str) -> int:
        cursor = self.connection.cursor()
        categoria_id = cursor.execute('INSERT INTO categoria (nome) VALUES (?)', (nome,)).lastrowid
        self.connection.commit()
        self.close_connection()
        return categoria_id
    
    def create_produto(self, id_estoque: int, id_categoria: int, nome: str, quantidade: int, preco_compra: float) -> int:
        cursor = self.connection.cursor()

        # Verificar se o id_estoque existe
        cursor.execute('SELECT id FROM estoque WHERE id = ?', (id_estoque,))
        if cursor.fetchone() is None:
            return {'error': True, 'message': 'O id_estoque informado não existe'}

        cursor.execute('INSERT INTO produto (id_estoque, id_categoria, nome, quantidade, preco_compra) VALUES (?, ?, ?, ?, ?)', (id_estoque, id_categoria, nome, quantidade, preco_compra))
        self.connection.commit()
        self.close_connection()
        return cursor.lastrowid


if __name__ == '__main__':

    query = """
CREATE TABLE IF NOT EXISTS estoque (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data DATE NOT NULL UNIQUE
);
CREATE TABLE IF NOT EXISTS categoria (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL UNIQUE
);
CREATE TABLE IF NOT EXISTS produto (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_estoque INTEGER NOT NULL,
    id_categoria INTEGER NOT NULL,
    nome TEXT NOT NULL,
    quantidade INTEGER NOT NULL,
    preco_compra REAL NOT NULL,
    FOREIGN KEY(id_estoque) REFERENCES estoque(id),
    FOREIGN KEY(id_categoria) REFERENCES categoria(id)
)
"""
    try:
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        cursor.executescript(query)
        connection.commit()
        connection.close()
        print("Banco de dados criadas com sucesso")
    except sqlite3.Error as e:
        print(f"Database error: {e}")

