import pymongo
from bson import ObjectId

dbName = "instagram-part-2"

def insert_data(data, collectionName):
    connection = open_connection()
    database = connection[dbName]
    collection = database[collectionName]
    collection.insert_one(data)
    close_connection(connection)

def fetch_data(collectionName, query):
    connection = open_connection()
    database = connection[dbName]
    collection = database[collectionName]
    documents = collection.find(query)
    close_connection(connection)
    return documents

def open_connection():
    connection = pymongo.MongoClient("localhost", 27017)
    return connection

def close_connection(connection):
    connection.close()