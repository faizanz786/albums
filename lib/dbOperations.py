import pymongo
from bson import ObjectId

def insert_data(data, collectionName):
    connection = open_connection()
    database = connection["instagram-part-2"]
    collection = database[collectionName]
    collection.insert_one(data)
    close_connection(connection)

def open_connection():
    connection = pymongo.MongoClient("localhost", 27017)
    return connection

def close_connection(connection):
    connection.close()