"""
1 0 0 0
1 1 0 0
1 1 1 0
1 1 1 1
"""
for r in range(4):
    for c in range(4):
        if c <= r:
            print(1,end=" ")
        else:
            print(0,end=" ")
    print()