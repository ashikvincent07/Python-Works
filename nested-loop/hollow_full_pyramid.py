
for r in range(1, 5):

    for c in range(1,8):

        if r+c == 5 or r==4 or c-r == 3:
            print("*",end=" ")
        else:
            print(" ",end=" ")

    print()