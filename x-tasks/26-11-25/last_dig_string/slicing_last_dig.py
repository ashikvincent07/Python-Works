file_path = "x-tasks/26-11-25/last_dig_string/numbers.txt"

fr = open(file_path, "r")

for num in fr:
    num = num.rstrip("\n")
    print(num[-1])