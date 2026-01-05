

for r in range(1, 6):

    for c in range(1, 5-r+1):
        print(" ",end=" ")

    for c in range(1, 2*r):
        print("*",end=" ")

    print()