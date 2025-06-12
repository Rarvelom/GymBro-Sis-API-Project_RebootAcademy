# main.py
from fastapi import FastAPI
from Gymbro.app.connection.database import connect_to_mongo, close_mongo_connection
from Gymbro.app.routes import spot_routes, user_routes, training_routes

app= FastAPI()
app.include_router(spot_routes.router, prefix="/api/v1", tags=["spots"])
app.include_router(user_routes.router, prefix="/api/v1", tags=["users"])
app.include_router(training_routes.router, prefix="/api/v1", tags=["training"])

# Connect to MongoDB when the application starts
@app.on_event("startup")
async def startup_event():
    global mongo_client
    mongo_client = connect_to_mongo()
    print("Database connection established.")


@app.on_event("shutdown")
async def shutdown_event():
    global mongo_client
    try:
        close_mongo_connection(mongo_client)
        print("Database connection closed.")
    except Exception as e:
        print(f"Error during shutdown: {e}")
      