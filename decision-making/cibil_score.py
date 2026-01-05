cibil_score = int(input("Enter cibil score: "))

if cibil_score in range(300, 550):
    print("POOR")

elif cibil_score in range(550, 650):
    print("AVERAGE")

elif cibil_score in range(650, 750):
    print("GOOD")

elif cibil_score in range(750, 901):
    print("EXCELLENT")

else :
    print("Invalid entry.")