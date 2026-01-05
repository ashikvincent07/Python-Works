principle_amount = int(input("Enter principle amount: "))

rate_of_interest = float(input("Enter rate of interest: "))

number_of_months = int(input("Enter tenure in months: "))

rate_of_interest = rate_of_interest / (12 * 100)

emi_amount = (principle_amount * rate_of_interest * (1 + rate_of_interest) ** number_of_months) / ((1 + rate_of_interest)
** number_of_months-1)

print(f"Emi amount = {round(emi_amount,2)}")
