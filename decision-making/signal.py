signal = input("Enter signal (red | greeen | yellow): ").lower()

if signal == "red":
    print("STOP XX")

elif signal == "green":
    print("GO >>")

elif signal == "yellow":
    print("WAIT !!")

else:
    print("Invalid Signal.")