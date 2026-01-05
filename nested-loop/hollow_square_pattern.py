n=5

for r in range(1, n+1):
    
    for c in range(1, n+1):

        if r == 1 or c == 1 or r == n :
            print("*",end=" ")

        elif c == 5:
            print((n+3)*" "+"*",end="")
        

    print()