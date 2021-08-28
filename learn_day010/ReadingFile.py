
path = "/RISHI/H2K/H2KProjects/SEDAP/CustomerWatchTime_04052020.csv"

file = open(path)
Entry_ID = 0
Customer_ID = 1
Customer_First_Name = 2


for eachRow in file:
    if len(str(eachRow).strip()) > 0:
        row = eachRow.split(',')
        result = validate_Customer_First_Name(row[Customer_First_Name])


def validate_Customer_First_Name(name):
    return "ErrorMessage"


'''
for i in range(1, 10):
    print(file.read(10))
'''