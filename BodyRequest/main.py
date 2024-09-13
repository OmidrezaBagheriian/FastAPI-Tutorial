from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Personal(BaseModel):
    name: str
    national_code: str
    price: float
    tax: Union[float, None] = None

@app.get("/person/")
async def person(personal: Personal):
    return personal