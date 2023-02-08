from pydantic import BaseModel
from typing import Optional, List
from src.schemas.response_schemas import ProdutoResponse, UsuarioResponse





class Usuario(BaseModel):
    id: Optional[int]= None
    nome: str
    telefone: str
    senha: str
    produtos: List[ProdutoResponse]
    class Config:
        orm_mode=True
    
class Produto(BaseModel):
    id: Optional[int]=None
       
    nome: str
    detalhes: str
    preco: float
    disponivel: bool = False
    usuario_id: Optional[int] 
    usuario:Optional[UsuarioResponse]
    class Config:
        orm_mode=True




# class Pedido(BaseModel):
#     id:Optional[str]+None   
    
#     quantidade:int
#     entrega:bool=True
#     endereco: str
#     observacoes: Optional[str]="Sem observações"
    
