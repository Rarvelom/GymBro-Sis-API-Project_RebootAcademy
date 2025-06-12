# CREATE SCHEMA FOR USER
from pydantic import BaseModel

class UserSchema(BaseModel):
    id: int # Unique identifier for the user
    username: str # Unique username for the user
    age: int # Age of the user
    sex: str 
    height: float # Height of the user in cm
    weight: float # Weight of the user in kg
    availability: str # Availability of the user (e.g., "available", "busy", "offline")
    description: str # Description of the user
    experience: str # Experience level of the user (e.g., "beginner", "intermediate", "advanced")

    class Config:
        orm_mode = True
        # This allows the model to work with ORM objects



    