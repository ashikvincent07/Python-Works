# Write a recursive function to find the factorial of a number.
number = int(input("Enter a number: "))

def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)

result = factorial(number)

print(result)