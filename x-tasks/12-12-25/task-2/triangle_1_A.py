"""
1 A A A
1 1 A A
1 1 1 A
1 1 1 1
"""

for r in range(4):
    for c in range(4):
        if c <= r:
            print(1,end=" ")
        else:
            print("A",end=" ")
        
    print()