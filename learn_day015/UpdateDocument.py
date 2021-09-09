import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
testdb_aug = myclient["testdatabase_aug21"]
test_collection = testdb_aug["august_deals_stores"]
myquery = { "store_number": "0141" }
newvalues = { "$set": { "store_name": "Perimeter Blvd" , "address" : "141 Perimeter Blvd"} }


x = test_collection.update_one(myquery, newvalues)
print(x.modified_count, " documents Updated.")

myclient.close()