import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
testdb_aug = myclient["testdatabase_aug21"]
test_collection = testdb_aug["august_deals_stores"]
myquery = { "store_number": { "$gt": "01" } }

for eachDoc in test_collection.find(myquery, {"_id" : 0, "store_number": 1, "store_name": 1}):
    print(eachDoc)

myclient.close()

