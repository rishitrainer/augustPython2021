'''
*args - optional parameter list
**kwargs
'''
def validation(cust_id, cust_name, cust_zipcode, **kwargs):
    print(cust_id, cust_name, cust_zipcode)
    for eachArg in kwargs:
        if eachArg == "address1":
            print("Handle String validation on address", kwargs.get(eachArg))
        print(eachArg, kwargs.get(eachArg))
        if eachArg == "mobile":
            if str(kwargs.get(eachArg)).isdigit() and len(str(kwargs.get(eachArg))) == 10:
                print("Valid MObile Number")


validation(1000, "David", "30080", address1="3375 Spring Hill Pkwy", city="Atlanta", mobile="7703809700", hobby="Hobbies")