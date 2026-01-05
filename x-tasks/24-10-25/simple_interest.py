principle_amount = int(input("Enter principle amount: "))

rate_of_interest = float(input("Enter rate of interest: "))

tenure = int(input("Enter tenure in years: "))

simple_interest = (principle_amount * rate_of_interest * tenure) / 100

print(f"Interest = {simple_interest}")