for r in range(1, 2*5):
    
    if r <= 5:

        for s in range(r, 5):
            print(" ",end="")

        for c in range(0, r):
            print("*",end=" ")

    else:
         for s in range(5, r):
            print(" ",end="")

         for c in range(r, 2*5):
            print("*",end=" ")




    print()