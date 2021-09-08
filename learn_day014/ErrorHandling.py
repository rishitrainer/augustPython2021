'''
Errors -
1. Programming Errors
2. User / Data Error

try:
    risky code which might throw an error
except:
    block of code which will execute when error is thrown by code

- Specific Error First, Genetic Error Later
- You can have any number of except blocks
- You can combine errors in single except block
'''

ingest = input("Enter One Number:")
answer = [100,200,300]
result = 0
try:
    if ingest.isnumeric():
        int_data = int(ingest)
        result = answer[int_data]/int_data
        print("This is a test print statement")
    else:
        print("Invalid Input Provided")
except (ZeroDivisionError, IndexError) as zex:
    print("KnownErrors:: There is an Error", zex)
except Exception as zex:
    print("Exception:: There is an Error", zex)
else:
    print("ELSE: Only when try completes without errors")
finally:
    print("finally:: This code always executes")


print("Answer is", result)