from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Atlas URI
# uri = "mongodb+srv://sidvjsingh:rlotm71La86YGv5d@mongodb.enotrvk.mongodb.net/?retryWrites=true&w=majority"

# local URI
uri = "mongodb://localhost:27017"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print("ERROR"+ e)