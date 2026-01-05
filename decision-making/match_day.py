day = int(input("Enter day(1 - 7): "))

match day:

    case 1:
        print("SUNDAY")

    case 2:
        print("MONDAY")
    
    case 3:
        print("TUESDAY")

    case 4:
        print("WEDNESDAY")

    case 5:
        print("THURSDAY")

    case 6:
        print("FRIDAY")

    case 7:
        print("SATURDAY")

    case _:
        print("Invalid entry.")