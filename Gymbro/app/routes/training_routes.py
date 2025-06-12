# Training Routes
from fastapi import APIRouter
from fastapi import HTTPException
from Gymbro.app.schema.training_schema import TrainingSchema
from Gymbro.app.controllers.training_controller import (
    get_training_by_type,
    get_all_training,
    create_training,
    update_training,
    get_training_by_level,
)

router = APIRouter()

@router.get("/training/{type}", response_model=list[TrainingSchema])
async def read_training(type: str):
    training = await get_training_by_type(type)
    if not training:
        raise HTTPException(status_code=404, detail="Training not found")
    return training


@router.get("/training")
async def read_all_training():
    training = await get_all_training()
    if not training:
        raise HTTPException(status_code=404, detail="No training found")
    return training

@router.get("/training/level/{level}", response_model=list[TrainingSchema])
async def read_training_by_level(level: str):
    training = await get_training_by_level(level)
    if not training:
        raise HTTPException(status_code=404, detail="Training not found for the specified level")
    return training

@router.post("/training")
async def create_new_training(training: TrainingSchema):
    training_data = training.dict()
    training_id = await create_training(training_data)
    return {"id": training_id, "message": "Training created successfully"}

@router.put("/training/{training_id}")
async def update_existing_training(training_id: str, training: TrainingSchema):
    training_data = training.dict()
    updated = await update_training(training_id, training_data)
    if not updated:
        raise HTTPException(status_code=404, detail="Training not found or update failed")
    return {"message": "Training updated successfully"}
# This code defines the routes for the training feature in the Gymbro application.  
# It includes endpoints to read, create, and update training data, with appropriate error handling.
# The routes are defined using FastAPI's APIRouter, and the controllers handle the business logic.