from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from dataManager import Datamanager
#remember to activate .venv and launch fastapi dev each time i load VSCodium 
    #source .venv/bin/activate
    #fastapi dev

server = FastAPI()

server.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"] 
)

dm = Datamanager()

@server.get('/')
def root():
    return {"message":"Hello World"}

@server.get('/getAllTodo')
def getAllTodo():
    return dm.getAllTodo()

@server.post('/createTodo')
async def createTodo(req:Request):
    data = await req.json()
    dm.createTodo(data)
    return {'status':'ok'}

@server.delete('/deleteOneTodo/{index}')
def deleteOneTodo(index:int):
    dm.deleteOneTodo(index)
    return {'status':'ok'} 

@server.delete('/deleteAllTodo')
def deleteAllTodo():
    return dm.deleteAllTodo()

@server.put('/updateOneTodo/{index}')
async def UpdateOneTodo(index:int, req:Request):
    currentData = await req.json()
    dm.updateOneTodo(index, currentData)
    return {'status':'ok'} 

