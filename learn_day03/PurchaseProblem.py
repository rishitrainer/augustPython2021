'''
Customer allowed for Purchase when age > 18 or state == FL
'''

age = 15
state = "FL"

check1 = (age > 18)
check2 = (state == "FL")

purchase = check1 or check2
print("Customer Purchase Answer is ", purchase)
'''
result= S1 or S2
S1  S2  result
T   T   T
T   F   T
F   T   T
F   F   F
'''