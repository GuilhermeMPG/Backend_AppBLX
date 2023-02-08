from pydantic import BaseModel
from typing import Optional, List
class ProdutoResponse(BaseModel):
    id:Optional[int] 
    nome: str
    preco: float
    detalhes: str

    class Config:
        orm_mode=True


class UsuarioResponse(BaseModel):
    id: Optional[int]= None
    nome: str
    telefone: str

    class Config:
        orm_mode=True