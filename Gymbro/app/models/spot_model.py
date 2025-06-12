# Create the Spot model for MongoDB
from Gymbro.app.connection.database import connect_to_mongo

db = connect_to_mongo()
spots_collection = db["spots"]
