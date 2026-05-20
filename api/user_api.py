from fastapi import FastAPI
from services.user_service import UserService

app = FastAPI()

user_service = UserService()

@app.get("/api/users")
def get_users():
    return user_service.get_users()

@app.post("/api/users")
def create_user(name: str, email: str):
    return user_service.create_user(
        name,
        email
    )
