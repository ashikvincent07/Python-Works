number = int(input("Enter number: "))

temp = number
digit = 0

while temp > 0:
    digit = temp%10
    print(digit)
    temp = temp//10
    