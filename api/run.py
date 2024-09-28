from typing import List
from fastapi import FastAPI

from database import DatabaseAPI
from schemas import *


app = FastAPI()


@app.get('/')
def read_root():
    return {'status_server': 1, 'message': 'API online'}

@app.get('/get-categorias', response_model=List[EsquemaCategoria])
def read_categorias():
    db = DatabaseAPI()
    categorias = db.get_categorias()
    return categorias

@app.get('/get-estoques', response_model=List[EsquemaEstoque])
def read_estoques():
    db = DatabaseAPI()
    estoques = db.get_estoques()
    return estoques

@app.get('/get-produtos/{estoque_id}', response_model=List[EsquemaProduto])
def read_produtos(estoque_id: int = 0):
    db = DatabaseAPI()
    produtos = db.get_produtos(estoque_id)
    return produtos

@app.post('/create-categoria')
def post_categoria(categoria: EsquemaCategoria):
    db = DatabaseAPI()
    id = db.create_categoria(categoria.nome)
    return id


@app.post('/create-estoque')
def post_estoque(estoque: EsquemaEstoque):
    db = DatabaseAPI()
    id = db.create_estoque(estoque.data)
    return id

@app.post('/create-produto')
def post_estoque(produto: EsquemaProduto):
    db = DatabaseAPI()
    id = db.create_produto(produto.id_estoque, produto.id_categoria, produto.nome, produto.quantidade, produto.preco_compra)
    return id

@app.delete('/delete-categoria/{id}')
def delete_categoria(id: int):
    db = DatabaseAPI()
    result = db.delete_categoria(id)
    return result

@app.delete('/delete-estoque/{id}')
def delete_estoque(id: int):
    db = DatabaseAPI()
    result = db.delete_estoque(id)
    return result

@app.delete('/delete-produto/{id}')
def delete_produto(id: int):
    db = DatabaseAPI()
    result = db.delete_produto(id)
    return result
