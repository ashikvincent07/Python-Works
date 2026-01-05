mark = int(input("Enter mark out 100: "))

if mark >= 40 and mark <= 100:
    print("Pass")
    if mark >= 90 :
        print("Distinction")
elif mark >= 0 and mark < 40 :
    print("Fail")
else :
    print("Invalid entry")