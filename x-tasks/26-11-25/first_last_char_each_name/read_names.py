file_path = "x-tasks/26-11-25/first_last_char_each_name/names.txt"

fr = open(file_path, "r")

for name in fr:
    name = name.rstrip("\n")
    print(f"Name : {name}, first char : {name[0]}, last char : {name[-1]} ")