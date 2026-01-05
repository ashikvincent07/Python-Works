n = int(input("Enter a number : "))

def reverse_num(n):
    if n == 0:
        return ""
    return str(n % 10) + reverse_num(n // 10)

print(reverse_num(n))
