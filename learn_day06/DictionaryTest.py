sampleDictionary = {
    "model": "Camry LE",
    "company": "Toyota",
    "year": 2015,
    "DMV" : 2015,
    "VIN": "V398247892374NHI",
    "listTest" : ["Apple", "Orange", "Pineapple"],
}

print(sampleDictionary)
print(sampleDictionary["model"])
print(sampleDictionary.get("company"))
sampleDictionary["color"] = "Grey"
print(sampleDictionary)
sampleDictionary["year"] = 2016
print(sampleDictionary)
sampleDictionary.pop("model")
print(sampleDictionary)
sampleDictionary.popitem()
print(sampleDictionary)

'''
for eachKey in sampleDictionary:
    print(eachKey, sampleDictionary.get(eachKey))
'''

for eachkey, eachValue in sampleDictionary.items():
    print(eachkey, eachValue)

for eachValue in sampleDictionary.values():
    print(eachValue)