num = int(input("Enter a number: "))

if num % 15 == 0 :
    print("fizzbuzz")

elif num % 5 == 0 :
    print("buzz")

elif num % 3 == 0 :
    print("fizz")

else :
    print(f"{num} is not divisible by 3, 5 or 15.")