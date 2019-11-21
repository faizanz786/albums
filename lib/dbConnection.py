import pymongo

class db_connection:
    mydb = None

    def connect():
        global mydb
        myclient = pymongo.MongoClient('localhost', 27017)
        mydb = myclient["instagram-part-2"]
        return mydb