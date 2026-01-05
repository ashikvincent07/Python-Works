def bmi(weight, height_in_cm):

    height_in_meter = height_in_cm / 100

    result = round(weight / (height_in_meter ** 2),2)

    return result


print(bmi(72,179))

