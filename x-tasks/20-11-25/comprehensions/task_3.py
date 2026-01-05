marks = {"Aju": 92, "Binu": 76, "Chandru": 64}

grades = {
    name: ("A" if score >= 90 else
           "B" if score >= 75 else
           "C" if score >= 60 else
           "D")
    for name, score in marks.items()
}

print(grades)
