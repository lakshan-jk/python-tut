# from pymongo import MongoClient
# client = MongoClient('localhost', 27017)
# db = client['mydb']
# print("Database created........")

# print("List of databases after creating new one")
# print(client.list_database_names())
# db.test_collection.insert_one({"hello": "world"})
# print(client.list_database_names())  # Now you should see 'mydb'

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['mydb']

# Insert dummy data to create DB
# db.test.insert_one({"msg": "wammala naan tha inga pooley!!!"})

collection = db['pythontut']
# collection.insert_one({"hello": "world"})
# doc = [{"name": "jesus", "age": "1000+", "createdAt": "2022-02-02"},
#        {"name": "james", "age": "1000+", "createdAt": "2022-02-02"},
#        {"name": "john", "age": "1000+", "createdAt": "2022-02-02"}]
# collection.insert_many(doc)
print(collection.find_one())

print(collection.find_one({"name": "jesus"}))
print("Database created........")
print("List of databases:")

print(client.list_database_names())
