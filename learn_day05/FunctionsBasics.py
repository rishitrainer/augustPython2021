'''
function - repeatable process block
i/p - parameter to function
o/p - return from the function

def function_name(parameters <optional>):
    body of function
    processing logic
    <optional> return
'''

def say_hello(name="Guest"):
    print("Hello", name)


def validation(cust_id, cust_name, cust_zipcode):
    print(cust_id, cust_name, cust_zipcode)
    validation_flag = True
    if str(cust_id).isdigit():
        int_custId = int(cust_id)
    else:
        validation_flag = False

    if not str(cust_name).isalpha():
        validation_flag = False

    if str(cust_zipcode).isnumeric() and len(str(cust_zipcode)) == 5:
        print("Valid Zipcode")
    else:
        validation_flag = False

    return validation_flag



say_hello(name="David") # Keyed parameter - passing key=value
say_hello("Neil")
say_hello(100)
print(type(say_hello))
is_valid = validation(cust_zipcode="30080", cust_id="10001", cust_name="Ri$hi")
print("Is Customer Valid", is_valid)