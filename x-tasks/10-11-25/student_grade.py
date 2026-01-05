def grade(mark) :
        
    if mark <= 100 and mark >= 0:

        if mark >= 90 :
            return "A"

        elif mark >= 75:
            return "B"

        elif mark >= 50:
            return "C"

        else :
            return "F"

    else:
        return "Invalid mark"


marks = int(input("Enter your mark (0 - 100) : "))

print(grade(marks))