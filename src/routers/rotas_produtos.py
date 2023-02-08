from fastapi import APIRouter
from fastapi import Depends, status
from typing import List
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db
from src.schemas.schemas import Produto
from src.schemas.response_schemas import ProdutoResponse
from src.infra.sqlalchemy.repositorios.repositorio_produto import RepositorioProduto



router = APIRouter()


@router.post('/produtos', status_code=status.HTTP_201_CREATED, response_model=ProdutoResponse)
def criar_produtos(produto:Produto, session: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(session).criar(produto)
    return produto_criado

@router.put('/produtos/{id}', status_code=status.HTTP_200_OK,response_model=ProdutoResponse)
def atualizar_produtos(id:int, produto:Produto, session: Session = Depends(get_db)):
    RepositorioProduto(session).editar(id, produto)
    produto.id = id
    return produto

@router.get('/produtos', status_code=status.HTTP_200_OK,response_model=List[Produto])
def listar_produtos(session: Session = Depends(get_db)):
    produtos = RepositorioProduto(session).listar()
    return produtos

@router.delete('/produtos/{id}',status_code=status.HTTP_200_OK)
def remover_produtos(id:int, session: Session=Depends(get_db)):
    RepositorioProduto(session).remover(id)
    return