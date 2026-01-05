age  = int(input("Enter age: "))

if age < 18:
    raise Exception("Invalid age")
else:
    print("Eligible for voting. ")