"""
R R R R
R S S R
R S S R
R R R R
"""

for r in range(4):
    for c in range(4):
        if r == 0 or r == 3:
            print("R",end=" ")
        elif (r == 1 or r == 2) and (c == 1 or c == 2):
            print("S",end=" ")
        else:
            print("R",end=" ")
    print()
