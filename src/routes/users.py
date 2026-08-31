from fastapi import FastAPI, APIRouter

users_router = APIRouter()

@users_router.get("/users")
def get_users():
    return {"message": "Fetching all users..."}