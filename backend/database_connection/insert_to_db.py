import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["white-port"]
print(mydb.list_collection_names())
user = mydb['user']