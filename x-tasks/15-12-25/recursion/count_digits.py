# ⿥ Write a recursive function to count the number of digits in a given number.
def count_digits(n):
    if n == 0:          
        return 0
    return 1 + count_digits(n // 10)


number = int(input("Enter a number: "))

print(count_digits(number))