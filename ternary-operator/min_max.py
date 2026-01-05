n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))

largest = n1 if n1 > n2 else n2

smallest = n1 if n1 < n2 else n2

print(f"Max : {largest}\nMin : {smallest}")