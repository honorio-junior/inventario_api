from typing import Optional
from pydantic import BaseModel
from datetime import date

class EsquemaCategoria(BaseModel):
    id: Optional[int] = None
    nome: str

class EsquemaEstoque(BaseModel):
    id: Optional[int] = None
    data: date

class EsquemaProduto(BaseModel):
    id: Optional[int] = None
    id_estoque: int
    id_categoria: int
    nome: str
    quantidade: int
    preco_compra: float

