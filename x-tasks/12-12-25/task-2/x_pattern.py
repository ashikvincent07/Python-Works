"""
1   0   0   0   1
0   1   0   1   0
0   0   1   0   0
0   1   0   1   0
1   0   0   0   1
"""

n = int(input("Enter number of rows: "))

for r in range(n):
    for c in range(n):
        if r == c:
            print(1,end=" ")
        elif r + c == n - 1:
            print(1,end=" ")
        else:
            print(0,end=" ")
    print()