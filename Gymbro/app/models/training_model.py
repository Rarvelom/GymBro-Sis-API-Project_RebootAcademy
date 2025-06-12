# Create the Training model for MongoDB
from Gymbro.app.connection.database import connect_to_mongo

db = connect_to_mongo()
training_collection = db["training"]