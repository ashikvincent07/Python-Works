number = int(input("Enter number: "))

while number != 0:
    
    digit = number%10

    print(digit**2)

    number = number//10