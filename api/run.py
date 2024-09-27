from typing import List
from fastapi import FastAPI

from database import get_categorias, get_estoques, get_produtos
from schemas import *


app = FastAPI()


@app.get('/')
def read_root():
    return {'status_server': 1, 'message': 'API online'}

@app.get('/get-categorias', response_model=List[EsquemaCategoria])
def read_categorias():
    categorias = get_categorias()
    return categorias

@app.get('/get-estoques', response_model=List[EsquemaEstoque])
def read_estoques():
    estoques = get_estoques()
    return estoques

@app.get('/get-produtos/{estoque_id}', response_model=List[EsquemaProduto])
def read_produtos(estoque_id: int = 0):
    produtos = get_produtos(estoque_id)
    return produtos

# @app.put('/items/{item_id}')
# def update_item(item_id: int, item: Item):
#     return {'item_name': item.name, 'item_id': item_id}

