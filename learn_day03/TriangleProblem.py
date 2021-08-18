'''
Triangle Problem side1, side2, side3
HW - Take sides as inputs - make sure they are integers
'''
side1=int(input("Enter Value of side 1"))
side2=int(input("Enter Value of side 2"))
side3=int(input("Enter Value of side 3"))

check1 = ((side1+ side2) > side3)
check2 = ((side1+ side3) > side2)
check3 = ((side2+ side3) > side1)
print("Check 1", check1)
print("Check 2", check2)
print("Check 3", check3)

result = check1 and check2 and check3
print("Triangle Formation Result ", result)
'''
result= S1 and S2
S1  S2  result
T   T   T
T   F   F
F   T   F
F   F   F
'''
