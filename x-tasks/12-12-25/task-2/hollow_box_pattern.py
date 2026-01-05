"""
1 1 1 1 1
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
1 1 1 1 1
"""
n = int(input("Enter number of rows: "))

for r in range(n):
    for c in range(n):
        if r == 0 or r == n - 1:
            print(1,end=" ")
        elif c == 0 or c == n - 1:
            print(1,end=" ")
        else:
            print(0,end=" ")
    print()
        