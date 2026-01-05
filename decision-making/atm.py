db_pin = 3214

db_balance = 5000

pin = int(input("Enter pin: "))

if db_pin == pin :
    amount = int(input("Enter amount: "))

    if amount <= db_balance :
        print("Transaction succesful.")

    else :
        print("Insufficient balance.")

else :
    print("Incorrect pin.")