# Create Schema for Spot in MongoDB
from pydantic import BaseModel

class SpotSchema(BaseModel):

    id: int  # Unique identifier for the spot
    user_id: int  # ID of the user who created the spot
    name: str  # Name of the spot
    location: str  # Location of the spot (e.g., "New York", "Los Angeles")
    description: str  # Description of the spot
    type: str  # Type of the spot (e.g., "gym", "park", "studio")
    schedule: str  # Schedule of the spot (e.g., "Monday-Friday 6am-10pm")

    class Config:
        orm_mode = True
        # This allows the model to work with ORM objects
        # Useful for converting ORM models to Pydantic models



        