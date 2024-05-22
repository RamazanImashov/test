from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

fake_users = [
    {'id': 1, 'role': "admin", 'name': 'Bot'},
    {'id': 2, 'role': 'user', 'name': 'John'},
    {'id': 3, 'role': 'trader', 'name': 'Sam'},
]


class User(BaseModel):
    id: int
    role: str
    name: str


@app.get("/users/{user_id}", response_model=list[User])
def get_user(user_id: int):
    return [user for user in fake_users if user.get('id') == user_id]


@app.get("/users", response_model=list[User])
def get_users():
    return fake_users
