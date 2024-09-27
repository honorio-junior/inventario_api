import sqlite3
import os
from typing import List, Dict

DATABASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database.sqlite')

def get_connection():
    return sqlite3.connect(DATABASE)

def fetch_all(query: str, params: tuple = ()) -> List[Dict]:
    try:
        with get_connection() as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute(query, params)
            return [dict(row) for row in cursor.fetchall()]
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []

def get_categorias() -> List[Dict]:
    return fetch_all('SELECT * FROM categoria')

def get_estoques() -> List[Dict]:
    return fetch_all('SELECT * FROM estoque')

def get_produtos(estoque_id: int) -> List[Dict]:
    return fetch_all('SELECT * FROM produto WHERE id_estoque = ?', (estoque_id,))



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
        with get_connection() as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.executescript(query)
            conn.commit()
            print("Tabelas criadas com sucesso")
    except sqlite3.Error as e:
        print(f"Database error: {e}")

