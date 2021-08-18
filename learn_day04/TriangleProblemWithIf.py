'''
Triangle Problem side1, side2, side3
HW - Take sides as inputs - make sure they are integers
'''
side1=int(input("Enter Value of side1 : "))
side2=int(input("Enter Value of side2 : "))
side3=int(input("Enter Value of side3 : "))


if ((side1+ side2) > side3) and ((side1+ side3) > side2) and ((side2+ side3) > side1):
    print("Triangle is Possible")
else:
    print("Triable is Not Possible")
