from fastapi import APIRouter
from fastapi import Depends, status, HTTPException
from typing import List
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db
from src.schemas.schemas import Usuario
from src.schemas.response_schemas import UsuarioResponse
from src.infra.sqlalchemy.repositorios.repositorio_usuario import RepositorioUsuario
from src.infra.providers import hash_provaider

router= APIRouter()


@router.post('/usuarios', status_code=status.HTTP_201_CREATED)
def criar_usuarios(usuario: Usuario, session: Session= Depends(get_db)):
#verifiar se o usuario ja existe para o telefone 
    usuario_localizado = RepositorioUsuario(session).obter_por_telefone(usuario.telefone)  
    if usuario_localizado:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Já existe um usuário para este telefone!")  
# criar usiario novo
    usuario.senha = hash_provaider.gerar_hash(usuario.senha)
    usuario_criado = RepositorioUsuario(session).criar(usuario)
    return usuario_criado

@router.get('/usuarios', status_code=status.HTTP_200_OK,response_model=List[Usuario])
def listar_usuarios(session: Session = Depends(get_db)):
    listaDeUsuarios = RepositorioUsuario(session).listar()
    return listaDeUsuarios