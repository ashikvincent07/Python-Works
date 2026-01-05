# Write a recursive function to find the sum of first N natural numbers.
limit = int(input("Enter limit: "))

def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n-1)

result = sum_n(limit)

print(result)
