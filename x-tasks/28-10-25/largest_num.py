number1 = int(input("Enter a number 1: "))

number2 = int(input("Enter a number 2: "))

if number1 > number2 :
    print(f"{number1} is largest number.")
elif number2 > number1 :
    print(f"{number2} is largest number.")
else :
    print("Both are equal.")