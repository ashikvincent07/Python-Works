day = int(input("Enter a day(1 - 7): "))

if day > 0 and day <=5 :
    print("Weekday")

elif day > 0 and day <= 7 :
    print("Weekend")
    
else :
    print("Invalid input")