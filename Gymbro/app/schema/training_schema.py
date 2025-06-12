from pydantic import BaseModel
from typing import Optional

class TrainingSchema(BaseModel):
    id: Optional[str] = None  # Unique identifier for the training session
    user_id: Optional[str] = None  # ID of the user who created the training session
    spot_id: Optional[str] = None  # ID of the spot where the training session is held
    type: Optional[str] = None  # Type of training (e.g., "strength", "cardio", "flexibility")
    datetime: Optional[str] = None  # Date and time of the training session in ISO format
    level: Optional[str] = None  # Level of the training session (e.g., "beginner", "intermediate", "advanced")
    description: Optional[str] = None  # Description of the training session

    class Config:
        orm_mode = True
