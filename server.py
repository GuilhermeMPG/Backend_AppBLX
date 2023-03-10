from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers import  rotas_produtos
from src.routers import  rotas_usuarios





app = FastAPI()

origins = ['http://localhost:3000',
           'https://myapp.vercel.com'
          ]
# criar_bd()
#CORS
app.add_middleware(CORSMiddleware,allow_origins=origins,
                                  allow_credentials=True,
                                  allow_methods=["*"],
                                  allow_headers=["*"]                            
)


#PRODUTOS
app.include_router(rotas_produtos.router)
#USUARIOS
app.include_router(rotas_usuarios.router)
