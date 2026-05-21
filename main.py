from fastapi import FastAPI
#remember to activate .venv each time i load VSCodium
    #source .venv/bin/activate

server = FastAPI()

@server.get('/')
def root():
    return {"message":"Hello World"}
