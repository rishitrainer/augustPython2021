'''
Adding 1 to 10

while condition:
    block of code (iteration) till condition is true
    condition modifier
'''

counter = 1
total = 0
while counter <= 10:
    print("Counter Value :: " , counter)
    total = total + counter
    # counter = counter + 1
    counter += 1

print("Counter value to terminate the loop ", counter)
print("Total ", total)