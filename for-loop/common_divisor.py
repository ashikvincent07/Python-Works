num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))
num3 = int(input("Enter number3: "))

small_number = min(num1, num2, num3)

print("Common divisors : ",end=" ")

for i in range(1, small_number+1):

    if num1 % i == 0 and num2 % i == 0 and num3 % i == 0 :
        print(i,end=" ")