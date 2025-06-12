# Spots Routes
from fastapi import APIRouter
from fastapi import HTTPException
from Gymbro.app.schema.spot_schema import SpotSchema
from Gymbro.app.controllers.spot_controller import get_spot_by_type, get_all_spots, create_spot, update_spot


router = APIRouter()

@router.get("/spots/{type}")
async def read_spot(type: str):
    spot = await get_spot_by_type(type)
    if not spot:
        raise HTTPException(status_code=404, detail="Spot not found")
    return spot

@router.get("/spots")
async def read_all_spots():
    spots = await get_all_spots()
    if not spots:
        raise HTTPException(status_code=404, detail="No spots found")
    return spots

@router.post("/spots")
async def create_new_spot(spot: SpotSchema):
    spot_data = spot.dict()
    spot_id = await create_spot(spot_data)
    return {"id": spot_id, "message": "Spot created successfully"}  

@router.put("/spots/{name}")
async def update_existing_spot(name: str, spot: SpotSchema):
    spot_data = spot.dict()
    updated = await update_spot(name, spot_data)
    if not updated:
        raise HTTPException(status_code=404, detail="Spot not found or update failed")
    return {"message": "Spot updated successfully"}


