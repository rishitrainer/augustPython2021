from learn_day014.CustomError import InvalidAgeError

def validate_age(age):
    if int(age) >= 18:
        print("Valid Customer")
        return True
    else:
        raise InvalidAgeError("Invalid Age Provided {}".format(age))

try:
    validate_age(2)
except InvalidAgeError as vr:
    print("InvalidAgeError :: ", vr)