from typing import Optional
from pydantic import BaseModel
from datetime import date

class SchemaCategoria(BaseModel):
    id: Optional[int] = None
    nome: str

class SchemaEstoque(BaseModel):
    id: Optional[int] = None
    data: date

class SchemaProduto(BaseModel):
    id: Optional[int] = None
    id_estoque: int
    id_categoria: int
    nome: str
    quantidade: int
    preco_compra: float

