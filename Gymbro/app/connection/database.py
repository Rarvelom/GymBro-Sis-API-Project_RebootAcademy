from pymongo import MongoClient
# connect to MongoDB
# gymbroDB
def connect_to_mongo():
    try:
        # Attempt to connect to MongoDB
        client = MongoClient("mongodb://localhost:27017/")
        db = client["gymbroDB"]
        print("Connected to MongoDB successfully.")
        return db
    except Exception as e:
        print(f"An error occurred while connecting to MongoDB: {e}")
        raise e
    
def close_mongo_connection(client):
    try:
        # Close the MongoDB connection
        client.close()
        print("MongoDB connection closed successfully.")
    except Exception as e:
        print(f"An error occurred while closing the MongoDB connection: {e}")
        raise e
    

