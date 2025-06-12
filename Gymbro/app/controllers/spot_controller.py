# controllers for the feature
from bson import ObjectId
from Gymbro.app.models.spot_model import spots_collection


async def get_spot_by_type(type: str):
    spot = spots_collection.find_one({"type": type})
    if spot:
        spot["_id"] = str(spot["_id"]) 
        spot["user_id"] = str(spot["user_id"]) if "user_id" in spot else None  # Convert ObjectId to string
    return spot

async def get_all_spots():
    spots = list(spots_collection.find())
    for spot in spots:
        spot["_id"] = str(spot["_id"])  # Convert ObjectId to string
        spot["user_id"] = str(spot["user_id"]) if "user_id" in spot else None
    return spots

async def create_spot(spot_data: dict):
    result = spots_collection.insert_one(spot_data)
    return str(result.inserted_id)  # Return the inserted spot's ID as a string

async def update_spot(name: str, spot_data: dict):
    result = spots_collection.update_one(
        {"name": name},
        {"$set": spot_data})
    return result.modified_count > 0  # Return True if the update was successful, False otherwise