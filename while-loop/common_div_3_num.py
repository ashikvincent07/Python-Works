num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))
num3 = int(input("Enter number3: "))

small = 0 

if num1 < num2 and num3:
    small = num1

elif num2 < num1 and num3:
    small = num2

else :
    small = num3

i = 1
print("Common divisors: ",end=" ")

while i <= small:

    if num1 % i == 0 and num2 % i ==0 and num3 % i == 0 :
        print(i,end=" ")

    i += 1