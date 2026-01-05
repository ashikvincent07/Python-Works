# Write a recursive function to find the greatest common divisor (GCD) of two numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

def gcd(a, b):
    if b == 0:          # base case
        return a
    return gcd(b, a % b)

print(gcd(a, b))
