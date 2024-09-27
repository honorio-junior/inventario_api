from typing import Optional
from pydantic import BaseModel

class EsquemaCategoria(BaseModel):
    id: Optional[int]
    nome: str

class EsquemaEstoque(BaseModel):
    id: Optional[int]
    data: str

class EsquemaProduto(BaseModel):
    id: Optional[int]
    id_estoque: int
    id_categoria: int
    nome: str
    quantidade: int
    preco_compra: float

