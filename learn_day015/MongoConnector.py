import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
testdb_aug = myclient["testdatabase_aug21"]
testdb = myclient["testdatabase"]

print(myclient.list_database_names())
print(testdb.list_collection_names())

test_collection = testdb_aug["august_deals_stores"]

oneStore = {
    "_id" : "1209382913",
    "store_number": "0111",
    "store_name": "Duluth Parkway",
    "address": "0111 Duluth Pwky"
}

mylist = [
    { "store_number": "0141", "store_name": "Perimeter Circle", "address": "141 Perimeter Circle" },
    { "store_number": "0131", "store_name": "Spring Hill", "address": "131 Spring Hill Pkwy" }
]


# result = test_collection.insert_one(oneStore)
result = test_collection.insert_many(mylist)
print(result.inserted_ids)

myclient.close()