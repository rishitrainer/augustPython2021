company = "H2KInfosys"
print("Outside function", company)

def drive_course():
    global company
    company = "IIT Workforce"
    print("Inside Function", company)

drive_course()
print("Outside function again", company)