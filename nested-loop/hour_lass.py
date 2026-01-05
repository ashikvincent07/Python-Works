for r in range(1, 2*5):

    if r <= 5:
        
        for s in range(0, r):
            print(" ",end="")

        for c in range(r, 5+1):
            print("*",end=" ")

    else:

        for s in range(r, 2*5):
            print(" ",end="")

        for c in range(5, r+1):
            print("*",end=" ")


    print()

