import pymongo
from bson import ObjectId

connection = pymongo.MongoClient("localhost", 27017)
database = connection["instagram-part-2"]

def insert_data(data, collectionName):
    collection = database[collectionName]
    collection.insert_one(data)

connection.close()