# Lists are written with square brackets.
sampleList = ["Apple", "Orange", "Pineapple"]
list_new = [
    {"item1" : "Value1"},
    {"item2" : "Value2"},
    {"item3" : "Value3"}
]

print(sampleList)
# Access Items: sampleList[1]
print(sampleList[0])
# Add Element: sampleList.append("newItem")
sampleList.append("Grapes")
print(sampleList)
#Add Indexed Element: sampleList.insert(1, "fruits")
sampleList.insert(1,"Strawberries")
print(sampleList)
# Allows Duplicates
sampleList.append("Grapes")
print(sampleList)
# Sorting: sampleList.sort()
sampleList.sort()
print("Sort :: " , sampleList)
# Remove Element: sampleList.remove("item")
sampleList.remove("Pineapple")
print(sampleList)
sampleList.pop(0)
print(sampleList)
# Check the Length: len(sampleList)
print(len(sampleList))

for eachItem in sampleList:
    print(eachItem)

if "orange" in sampleList:
    print("oranges are taken")

# Clear List: sampleList.clear()
sampleList.clear()
print(sampleList)

del sampleList
print(sampleList)