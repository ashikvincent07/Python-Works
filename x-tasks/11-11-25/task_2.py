years = [2021, 1999, 1920, 2024, 1852, 1991, 2026, 2000, 2023, 2016, 2009]

print("Leap years: ",end="")

for year in years:

    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print(year,end=", ")