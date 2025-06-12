# Create the Users model for MongoDB
from Gymbro.app.connection.database import connect_to_mongo

db = connect_to_mongo()
users_collection = db["users"]