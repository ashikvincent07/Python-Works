years=[2005,2004,2008,2010,2024,2028,2024,2005]

leap_years = [year for year in years if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)]

leap_year_count = {year : leap_years.count(year) for year in leap_years}

recursive_leap_year = {k for k, v in leap_year_count.items() if v > 1}

print(recursive_leap_year)