from fastapi import APIRouter
from fastapi import Depends, status, HTTPException
from typing import List
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db
from src.schemas.schemas import Usuario, LoginData, LoginSucesso
from src.schemas.response_schemas import UsuarioResponse
from src.infra.sqlalchemy.repositorios.repositorio_usuario import RepositorioUsuario
from src.infra.providers import hash_provaider, token_provaider
from src.routers.auth_utils import obter_usuario_logado

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

@router.post('/token', response_model=LoginSucesso)
def login(login_data: LoginData, session: Session = Depends(get_db)):
    senha = login_data.senha
    telefone = login_data.telefone
    usuario = RepositorioUsuario(session).obter_por_telefone(telefone)
    if not usuario:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Telefone ou senha estão incorretas!')
    senha_valida = hash_provaider.verificar_hash(senha, usuario.senha)
    if not senha_valida:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Telefone ou senha estão incorretas!')

# Gerar Token JWT
    token = token_provaider.criar_acess_token({'sub':usuario.telefone})
    return LoginSucesso(usuario = usuario, access_token = token)


@router.get('/me', response_model=UsuarioResponse)
def me(ususario: Usuario = Depends(obter_usuario_logado) , session: Session = Depends(get_db)):
    return ususario



