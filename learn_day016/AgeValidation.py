
class InvalidAgeError(Exception):
    pass

def validate_age(age):
    if str(age).isnumeric():
        if int(age) >= 18:
            return True
        else:
            return False
    else:
        raise InvalidAgeError("Invalid Age Provided")
'''
1. Positive - 20 - True
2. Negative - 8 - False
3. Boundary - 18 - True

'''