db_password = "654321"

db_otp = 8989

password = input("Enter password :" )

if db_password == password :
    otp = int(input("Enter otp: "))

    if db_otp == otp :
        print("Login succesful✅")

    else :
        print("Incorrect otp❌")

else :
    print("Incorrect password❌")