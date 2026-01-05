age = int(input("Enter age : "))

if age < 0 :
    raise Exception("invalid age")
else:
    print("ok")