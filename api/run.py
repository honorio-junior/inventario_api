from typing import List
from fastapi import FastAPI

from database import DatabaseAPI
from schemas import *


app = FastAPI()


@app.get('/')
def read_root():
    return {'url_docs': '127.0.0.1:8000/docs'}

@app.get('/get-categorias', response_model=List[SchemaCategoria])
def read_categorias():
    db = DatabaseAPI()
    categorias = db.get_categorias()
    return categorias

@app.get('/get-estoques', response_model=List[SchemaEstoque])
def read_estoques():
    db = DatabaseAPI()
    estoques = db.get_estoques()
    return estoques

@app.get('/get-produtos/{estoque_id}', response_model=List[SchemaProduto])
def read_produtos(estoque_id: int = 0):
    db = DatabaseAPI()
    produtos = db.get_produtos(estoque_id)
    return produtos

@app.post('/create-categoria')
def post_categoria(categoria: SchemaCategoria):
    db = DatabaseAPI()
    id = db.create_categoria(categoria.nome)
    return id


@app.post('/create-estoque')
def post_estoque(estoque: SchemaEstoque):
    db = DatabaseAPI()
    id = db.create_estoque(estoque.data)
    return id

@app.post('/create-produto')
def post_estoque(produto: SchemaProduto):
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

@app.put('/update-categoria/')
def update_categoria(categoria: SchemaCategoria):
    db = DatabaseAPI()
    result = db.update_categoria(categoria)
    return result

@app.put('/update-produto/')
def update_produto(produto: SchemaProduto):
    db = DatabaseAPI()
    result = db.update_produto(produto)
    return result
