num1 = int(input("Enter number 1: "))

num2 = int(input("Enter number 2: "))

last_dig_num1 = num1 % 10

last_dig_num2 = num2 % 10

sum = last_dig_num1 + last_dig_num2

print(sum > 5)