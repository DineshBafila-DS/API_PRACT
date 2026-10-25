from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()

class substractmodel(BaseModel):
    a:int
    b:int
def substract(a:int,b:int):
    return a-b 

@app.post("/dinesh/substract_pydantic/")
def sub_num(model:substractmodel):
    return substract(model.a,model.b)
