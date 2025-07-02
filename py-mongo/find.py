from db_config import get_db

db = get_db()
print(db)
coll = db["test"]

pipeline = [
    {'$match': {'name': 'vis'}}, 
    # {'$project': {'_id': 0, 'name': 1}} 
]

for doc in coll.aggregate(pipeline):
    print(doc["name"])
