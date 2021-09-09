import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
testdb_aug = myclient["testdatabase_aug21"]
test_collection = testdb_aug["august_deals_stores"]
myquery = { "store_number" : "0111" }

x = test_collection.delete_one(myquery)
print(x.deleted_count, " documents deleted.")

myclient.close()