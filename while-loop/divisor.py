num = int(input("Enter number: "))

i = 1

print("Divisors: ",end=" ")

while i <= num:

    if num % i == 0 :
        print(i,end=" ")

    i += 1