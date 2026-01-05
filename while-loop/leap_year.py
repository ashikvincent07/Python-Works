year = 1800

while year <= 2025:
    
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) :
        print(year,end=" ")

    year += 1