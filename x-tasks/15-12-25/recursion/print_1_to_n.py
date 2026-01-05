n = int(input("Enter a number: "))

def print_1_to_n(i, n):
    if i > n:
        return
    print(i)
    return print_1_to_n(i + 1, n)

print_1_to_n(1, n)
    