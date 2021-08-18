first = 1000
second = 200
third = 300
forth = 400

# To Find Biggest number out of four (- they are not equal)
'''
1. first > second , first > third --> First is Biggest
2. second > third --> Second is Biggest
3. third is Biggest
'''

if (first > second) and (first > third):
    print("First is Biggest")
elif second > third:
    print("Second is Biggest", second)
else:
    print("Third is Biggest", third)


