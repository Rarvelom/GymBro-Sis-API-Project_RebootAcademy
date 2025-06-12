# controllers for the feature
from bson import ObjectId
from Gymbro.app.models.training_model import training_collection

async def get_training_by_type(type: str):
    training = list(training_collection.find({"type": type}))
    for t in training:
        t["_id"] = str(t["_id"])
        t["spot_id"] = str(t["spot_id"]) if "spot_id" in t else None  # Convert ObjectId to string
        t["user_id"] = str(t["user_id"]) if "user_id" in t else None  # Convert ObjectId to string
    return training 

async def get_all_training():
   training = list(training_collection.find())
   for t in training:
      t["_id"] = str(t["_id"])
      t["spot_id"] = str(t["spot_id"]) if "spot_id" in t else None  # Convert ObjectId to string
      t["user_id"] = str(t["user_id"]) if "user_id" in t else None  # Convert ObjectId to string  # Convert ObjectId to string
   return training

async def get_training_by_level(level: str):
    training = list(training_collection.find({"level": level}))
    for t in training:
        t["_id"] = str(t["_id"])  # Convert ObjectId to string
        t["spot_id"] = str(t["spot_id"]) if "spot_id" in t else None
        t["user_id"] = str(t["user_id"]) if "user_id" in t else None
    return training

async def create_training(training_data: dict):
    result = training_collection.insert_one(training_data)
    return str(result.inserted_id)  # Return the inserted training's ID as a string

async def update_training(training_id: str, training_data: dict):
    result = training_collection.update_one(
        {"_id": (training_id)},
        {"$set": training_data})
