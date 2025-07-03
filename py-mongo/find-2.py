from db_config import get_db

db = get_db()
print(db)
coll = db["test"]

sample_data = [
    { "item": "apple", "category": "fruit", "price": 1.20, "quantity": 50},
    { "item": "banana", "category": "fruit", "price": 0.50, "quantity": 100},
    { "item": "carrot", "category": "vegetable", "price": 0.80, "quantity": 75},
    { "item": "apple", "category": "fruit", "price": 1.50, "quantity": 30},
    { "item": "milk", "category": "dairy", "price": 3.00, "quantity": 40},
    { "item": "cheese", "category": "dairy", "price": 5.00, "quantity": 25},
    { "item": "carrot", "category": "vegetable", "price": 0.90, "quantity": 60}
]


coll.insert_many(sample_data)

# Example 1: $match - Filtering Documents

pipeline_match=[
    {
        "$match": {
            "category": "fruit", "price":{'$gte': 1.00}
        }
    }
]
print("\n---- Fruits with price >= 1.00 ----")
for doc in coll.aggregate(pipeline_match):
    print(doc)


pipeline_group =[{
    "$group":{
        "_id": "$category",
        "total_quantity": {"$sum": "$quantity"},
        "total_price": {"$sum": {"$multiply": ["$price", "$quantity"]}},
        "average_price": {"$avg": "$price"}
    }
}]
print("\n---- Group by category ----")
for doc in coll.aggregate(pipeline_group):
    print(doc)
    

pipeline_project =[
    {"$match":{
        "age":{"$exists":False}
    }},
    {
        "$project":{
            "_id":0,
            "product_name": "$item",
            "item_price": "$price",
            "item_quantity": "$quantity"
        }
    }
]
print("\n---- Projecting fields ----")
for doc in coll.aggregate(pipeline_project):
    print(doc)
    
pipeline_sort =[
    {"$sort":{
        "price": -1
    }},
    {
        "$limit": 2
    }
]

print("\n---- Sorting and limiting ----")
for doc in coll.aggregate(pipeline_sort):
    print(doc)
    

pipeline_multi_stage = [
    {'$match': {'category': 'fruit'}},
    {
        '$group': {
            '_id': '$item',
            'total_quantity': {'$sum': '$quantity'}
        }
    },
    {'$match': {'total_quantity': {'$gt': 10}}},
    {'$sort': {'total_quantity': -1}}
]

print("\n---- Multi stage pipeline ----")
for doc in coll.aggregate(pipeline_multi_stage):
    print(doc)
    