from fastapi import FastAPI, Request
from dataManager import Datamanager
#remember to activate .venv and launch fastapi dev each time i load VSCodium 
    #source .venv/bin/activate
    #fastapi dev

server = FastAPI()
dm = Datamanager()

@server.get('/')
def root():
    return {"message":"Hello World"}

@server.get('/getAllTodo')
def getAllTodo():
    return 'initbruv'

@server.post('/createTodo')
async def createTodo(req:Request):
    data = await req.json()
    dm.createTodo(data)
    return {'status':'ok'}

@server.delete('/deleteOneTodo/{index}')
def deleteOneTodo(index:int):
    dm.deleteOneTodo(index)
    return {'status':'ok'} 

@server.put('/updateOneTodo/{index}')
async def UpdateOneTodo(index:int, req:Request):
    currentData = await req.json()
    dm.updateOneTodo(index, currentData)
    return {'status':'ok'} 

