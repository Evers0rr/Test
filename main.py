from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from typing import List

app =  FastAPI()

class User(BaseModel):
    id: int
    username: str
    email: EmailStr

users: List[User] = [
    User(id=1, username="dog", email="cooldog@gmail.com"),
    User(id=2, username="cat", email="coolcat@gmail.com"),
]

@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="Користувач не знайден")

@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="Користувач не знайден")

class CreateUserRequest(BaseModel):
    username: str
    email: EmailStr

@app.post("/create_user", response_model=User)
def create_user(user: CreateUserRequest):
    new_id = max(u.id for u in users) + 1 if users else 1
    new_user = User(id=new_id, username=user.username, email=user.email)
    users.append(new_user)
    return new_user








