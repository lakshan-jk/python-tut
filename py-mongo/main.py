from db_config import get_db

db = get_db()
print(db)
coll = db["test"]

data = [
    {"name": "Lakshan", "age": 30},
    {"name": "Lakshan", "age": 24}
]

try:
    coll.insert_many(data)
    print("Data inserted successfully")
except Exception as e:
    print("An exception occurred:", e)
