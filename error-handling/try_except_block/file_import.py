file_path = "error-handling/abc.txt"

try:
    fr = open(file_path, "r")

    for line in fr:
        print(fr)
except Exception as e:
    print(e)
finally:
    print("db commit")