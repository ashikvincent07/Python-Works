n = int(input("Enter a number: "))
p = int(input("Enter power: "))

def power_of_num(n, p):
    if p == 0:           
        return 1
    return n * power_of_num(n, p - 1)

print(power_of_num(n, p))
