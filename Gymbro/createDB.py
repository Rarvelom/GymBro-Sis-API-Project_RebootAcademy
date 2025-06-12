# Create Database in MongoDB to export to Compass
from pymongo import MongoClient

def create_database():
    # Connect to MongoDB
    client = MongoClient('mongodb://localhost:27017/')
    
    # Create a new database
    db = client['gymbroDB']
    
    # Create collections
    db.create_collection('users')
    db.create_collection('spots')
    db.create_collection('training')
    
    print("Database and collections created successfully.")
if __name__ == "__main__":
    create_database()
