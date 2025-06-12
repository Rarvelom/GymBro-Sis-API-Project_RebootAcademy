# controllers for the feature
from bson import ObjectId
from Gymbro.app.models.user_model import users_collection

async def get_user_by_username(username: str):
    user= users_collection.find_one({"username": username})
    if user:
        user["_id"] = str(user["_id"])
    # Convert ObjectId to string
    return user

async def get_all_users():
   user = list(users_collection.find())
   for u in user:
       u["_id"] = str(u["_id"])  # Convert ObjectId to string
   return user

async def create_user(user_data: dict):
    result= users_collection.insert_one(user_data)
    return str(result.inserted_id)  # Return the inserted user's ID as a string


async def update_user(username: str, user_data: dict):
    result = users_collection.update_one(
        {"username": username},
        {"$set": user_data})
    return result.modified_count > 0  # Return True if the update was successful, False otherwise