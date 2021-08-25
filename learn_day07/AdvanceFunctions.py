def shout(text):
    return str(text).upper()

def calculator(fn_name, num1, num2):
    result = 0
    def addition():
        result = num1 + num2
        print(result)

    def subtraction():
        result = num1 - num2
        print(result)

    def division():
        result = num1 / num2
        print(result)

    def multiplication():
        result = num1 * num2
        print(result)

    if fn_name == "+":
        return addition
    elif fn_name == "-":
        return subtraction
    elif fn_name == "*":
        return multiplication
    else:
        return division


print(shout("This is Me, Python"))
greet = shout
print(greet("See My Magic"))
fn_add = calculator("*", 10, 10)
fn_add()