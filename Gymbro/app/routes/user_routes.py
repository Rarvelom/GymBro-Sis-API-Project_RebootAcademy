# User Routes
from fastapi import APIRouter
from fastapi import HTTPException
from Gymbro.app.schema.user_schema import UserSchema
from Gymbro.app.controllers.user_controller import (
    get_user_by_username,
    get_all_users,
    create_user,
    update_user,
)
router = APIRouter()

@router.get("/users/{username}")
async def read_user(username: str):
    user = await get_user_by_username(username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/users")     
async def read_all_users():
    users = await get_all_users()
    if not users:
        raise HTTPException(status_code=404, detail="No users found")
    return users

@router.post("/users")
async def create_new_user(user: UserSchema):
    user_data = user.dict()
    user_id = await create_user(user_data)
    return {"id": user_id, "message": "User created successfully"}

@router.put("/users/{username}")       
async def update_existing_user(username: str, user: UserSchema):
    user_data = user.dict()
    updated = await update_user(username, user_data)
    if not updated:
        raise HTTPException(status_code=404, detail="User not found or update failed")
    return {"message": "User updated successfully"}


# This code defines the routes for the user feature in the Gymbro application.
# It includes endpoints to read, create, and update user data, with appropriate error handling.
# The routes are defined using FastAPI's APIRouter, and the controllers handle the business logic.