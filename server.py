from fastapi import FastAPI, Request, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from src.routers import rotas_auth
from src.routers import  rotas_produtos,rotas_pedidos
from src.jobs.write_notification import write_notification






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
#SEGURANÇA
app.include_router(rotas_auth.router, prefix='/auth')
#PEDIDOS
app.include_router(rotas_pedidos.router)

@app.post("/send_email/{email}")
def send_email(email:str, background:BackgroundTasks):
    background.add_task(write_notification, email, 'Olá tudo bem?!')
    return {'OK': 'Mensagem enviada'}


#MIDDLEWARES
@app.middleware('http')
async def processar_tempo_requisicao(request: Request, next):
    print('Interceptou Chegada...')
    response = await next(request)
    print('Interceptou a Volta...')
    return response
