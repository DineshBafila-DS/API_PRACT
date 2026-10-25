from fastapi import FastAPI
app=FastAPI()

@app.get("/dinesh/get_method/")
def add(a:int,b:int):
    return a+b

@app.post("/dinesh/post_method")
def sub(a:int, b:int):
    return a-b
