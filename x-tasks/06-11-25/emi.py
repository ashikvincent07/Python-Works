def emi_calc(amount, tenure, rate):


    rate = rate / (12 * 100)

    emi_amount = round((amount * rate * (1 + rate) ** tenure) / ((1 + rate)** tenure-1),0)

    return emi_amount

print(emi_calc(100000, 12, 10))# tenure in months