from fastapi import APIRouter
from fastapi import Depends, status, HTTPException
from typing import List
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db
from src.schemas.schemas import Pedido
from src.infra.sqlalchemy.repositorios.repositorio_pedido import RepositorioPedido

router = APIRouter() 
@router.post('/pedidos', status_code= status.HTTP_201_CREATED, response_model =Pedido)
def fazer_pedido(pedido:Pedido, session: Session= Depends(get_db)):
    pedido_criado = RepositorioPedido(session).gravar_pedido(pedido)
    return pedido_criado
@router.get('/pedidos/{id}', status_code= status.HTTP_200_OK , response_model=Pedido)
def exibir_pedido(id:int,session: Session= Depends(get_db)):
    try:
        pedidos = RepositorioPedido(session).buscar_por_id(id)
        return pedidos
    except:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"Não existe um pedido com id = {id}")
@router.get('/pedidos/{usuario_id}/compras', status_code= status.HTTP_200_OK , response_model=List[Pedido] )
def listar_pedidos(usuario_id:int,session: Session= Depends(get_db)):
    pedidos = RepositorioPedido(session).listar_meus_pedidos_por_usuario_id(usuario_id)
    return pedidos
@router.get('/pedidos/{usuario_id}/vendas', status_code=status.HTTP_200_OK , response_model=List[Pedido])
def listar_vendas(usuario_id=int, session: Session= Depends(get_db)):
    pedidos = RepositorioPedido(session).listar_minhas_vendas_por_usuario_id(usuario_id)
    return pedidos