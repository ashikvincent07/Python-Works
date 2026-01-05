"""
0 0 1 0 0
0 0 1 0 0
1 1 1 1 1
0 0 1 0 0
0 0 1 0 0
"""
for r in range(5):
    for c in range(5):
        if r == 2 or c == 2:
            print(1,end=" ")
        else:
            print(0,end=" ")
    print()