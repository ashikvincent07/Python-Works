day = int(input("Enter a day(1 - 7): "))

if day in range(1, 6):
    print("Weekday")

elif day in range(6, 8) :
    print("Weekend")
    
else :
    print("Invalid input")