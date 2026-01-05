number = int(input("Enter a number: "))

i = 1
factorial = 1

while i <= number :
    factorial *=  i
    i += 1

print(f"Factorial of {number} is {factorial}")