num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))

small = num1 if num1 < num2 else num2

# if num1 < num2:
#     small = num1

# else:
#     small = num2

i = 1

print("Common divisors: ",end=" ")

while i <= small:

    if num1 % i == 0 and num2 % i == 0:
        print(i,end=" ")

    i += 1