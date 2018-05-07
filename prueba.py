import pymongo
from pymongo import MongoClient
MONGODB_URI = 'mongodb://arquitectura_admin:123asdZXC@ds115340.mlab.com:15340/arquitectura'
client = MongoClient(MONGODB_URI, connectTimeoutMS=30000)
db = client.get_database("arquitectura")
twitter = db.Twitter
record =  twitter.find_one({"name":"mario"})
print(record)
data = {'name': 'luis antonio'}
twitter.insert_one(data)

