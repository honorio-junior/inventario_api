import sqlite3
import pathlib
from typing import List, Dict
from schemas import EsquemaCategoria, EsquemaProduto

DATABASE = pathlib.Path(__file__).parent / 'database.sqlite'

class DatabaseAPI:
    def __init__(self):
        self.connection = sqlite3.connect(DATABASE)
        self.connection.row_factory = sqlite3.Row
        self.connection.execute('PRAGMA foreign_keys = ON')

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
        try:
            estoque_id = cursor.execute('INSERT INTO estoque (data) VALUES (?)', (data,)).lastrowid
        except sqlite3.Error as e:
            self.close_connection() 
            return {e}
        self.connection.commit()
        self.close_connection()
        return estoque_id
    
    def create_categoria(self, nome: str) -> int:
        cursor = self.connection.cursor()
        try:
            categoria_id = cursor.execute('INSERT INTO categoria (nome) VALUES (?)', (nome,)).lastrowid
        except sqlite3.Error as e:
            self.close_connection()
            return {e}
        self.connection.commit()
        self.close_connection()
        return categoria_id
    
    def create_produto(self, id_estoque: int, id_categoria: int, nome: str, quantidade: int, preco_compra: float) -> int:
        cursor = self.connection.cursor()
        try:
            cursor.execute('INSERT INTO produto (id_estoque, id_categoria, nome, quantidade, preco_compra) VALUES (?, ?, ?, ?, ?)', (id_estoque, id_categoria, nome, quantidade, preco_compra))
        except sqlite3.Error as e:
            self.close_connection()
            return {e}
        self.connection.commit()
        self.close_connection()
        return cursor.lastrowid

    def delete_categoria(self, id: int) -> bool:
        cursor = self.connection.cursor()
        try:
            cursor.execute('DELETE FROM categoria WHERE id = ?', (id,))
            self.connection.commit()
        except sqlite3.Error as e:
            self.close_connection()
            return {e}
        self.close_connection()
        return True
    
    def delete_estoque(self, id: int) -> bool:
        cursor = self.connection.cursor()
        try:
            cursor.execute('DELETE FROM estoque WHERE id = ?', (id,))
            self.connection.commit()
        except sqlite3.Error as e:
            self.close_connection()
            return {e}
        self.close_connection()
        return True
    
    def delete_produto(self, id: int) -> bool:
        cursor = self.connection.cursor()
        try:
            cursor.execute('DELETE FROM produto WHERE id = ?', (id,))
            self.connection.commit()
        except sqlite3.Error as e:
            self.close_connection()
            return {e}
        self.close_connection()
        return True
    
    def update_categoria(self, categoria: EsquemaCategoria) -> int:
        cursor = self.connection.cursor()
        try:
            result = cursor.execute('UPDATE categoria SET nome = ? WHERE id = ?', (categoria.nome, categoria.id)).rowcount
            self.connection.commit()
        except sqlite3.Error as e:
            self.close_connection()
            return {e}
        self.close_connection()
        return result
    
    def update_produto(self, produto: EsquemaProduto) -> int:
        cursor = self.connection.cursor()
        try:
            result = cursor.execute('UPDATE produto SET id_estoque = ?, id_categoria = ?, nome = ?, quantidade = ?, preco_compra = ? WHERE id = ?', (produto.id_estoque, produto.id_categoria, produto.nome, produto.quantidade, produto.preco_compra, produto.id)).rowcount
        except sqlite3.Error as e:
            self.close_connection()
            return {e}
        self.connection.commit()
        self.close_connection()
        return result


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
    FOREIGN KEY(id_estoque) REFERENCES estoque(id) ON DELETE RESTRICT,
    FOREIGN KEY(id_categoria) REFERENCES categoria(id) ON DELETE RESTRICT
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

