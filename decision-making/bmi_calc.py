weight_in_kg = int(input("Enter weight in kg: "))

height_in_cm = int(input("Enter height in cm: "))

height_in_meter = height_in_cm/100

bmi = round(weight_in_kg / (height_in_meter ** 2),0)

print(f"BMI = {bmi}")

if bmi < 20 :
    print("Under Weight")

elif bmi < 25 :
    print("Normal Weight")

elif bmi < 30 :
    print("Over Weight")

elif bmi >= 30 :
    print("Obese")