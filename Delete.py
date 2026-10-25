from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
user_db={1:{"name":"dinesh", "age":28},
         2:{"name":"deepak", "age":25},
         3:{"name":"shiv", "age":28}
         }

#class User (BaseModel):
#    name:str
#    age:int

@app.delete("/user/dines/delete/v1/{user_id}")
def delete_user(user_id:int):
 if user_id in user_db:
  del user_db[user_id]
  return{"message":"message deleted successfully"}
 else:
   return{"message":"user not found"}
