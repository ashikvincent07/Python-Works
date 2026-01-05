for r in range(1, 6):

    for s in range(5-r, 0, -1):
        print(" ",end=" ")

    for c in range(0, r):
        print("*",end=" ")

    print()