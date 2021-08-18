name = "Hello, World!"

# Array of Characters
print(name)
print(name[1])
print(name[-4])
print(name[0:5]) # 0 - inclusive 5 : excluded
print(name[-6:-1]) # -6 - inclusive -1 : excluded
# reverse entire string in single command
print(name[::-1])

age = "21"
print(age.isnumeric())
print(age.isdigit())

print("name.upper() :: " , name.upper())
print("name.lower() :: " , name.lower())
print("name.capitalize() :: " , name.capitalize())
print(" name.find(\"W\") :: " , name.find("W"))
print("name.find(\"Z\") :: " , name.find("Z"))
print("name.count(o) :: " , name.count("o"))

statement = "Student {} is Passed with {} marks from {} class"
print(statement.format("Rishi", "80", "Python"))

print(name.isupper())
print(name.islower())
print(name.isalpha())
print(age.isalpha())
print("   test    ".strip())
print(name.split(","))

paragraph = "This is an \t interesting story \nThis is a new \bLine \nI have added in Story"
print(paragraph)