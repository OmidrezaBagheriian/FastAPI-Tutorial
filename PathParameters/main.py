
from fastapi import FastAPI

app = FastAPI()

@app.get("/{name}/")
async def root(name:str):
    return {"messages": f'{name}, Welcome to FastAPI.'}