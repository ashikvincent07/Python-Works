number = int(input("Enter number: "))

largest_odd = 0
temp = number
digit = 0

while temp != 0 :
    digit = temp % 10
    
    if digit % 2 != 0 and digit > largest_odd:
        largest_odd = digit

    temp = temp // 10

    if temp % 2 != 0 and temp > largest_odd:
        largest_odd = temp

if largest_odd != 0:
     print(largest_odd)
    
else:
    print("No Odd number digits")
   