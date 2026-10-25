from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
user_db={1:{"name":"dinesh", "age":28},
         2:{"name":"deepak", "age":25},
         3:{"name":"shiv", "age":28}
         }

class User (BaseModel):
    name:str
    age:int

@app.put("/user_db/data/V1/{user_id}")
def user_update(user_id:int,user:User):
    if user_id in user_db:
        user_db[user_id]=user.dict()
        return{"message":"user updated succeefully", "user":user_db[user_id]}
    else:
        return{"message":"user not found"}
