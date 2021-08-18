'''
Adding 1 to 10

for eachSample in values:
    block code for every sample in values data structure

range (start, end, step)
start - included
end - last + 1
step = jump
'''
data = ["apples", "oranges", "bananas"]

for eachFruit in data:
    print(eachFruit)

total = 0
for eachSampe in range(1,21,2):
    print("EachValue", eachSampe)
    total = total + eachSampe

print("Total", total)

for eachChara in "Hello, World!":
    print(eachChara)