file_path = "x-tasks/26-11-25/last_dig/numbers.txt"

fr = open(file_path, "r")

last_dig = {int(num): int(num)%10 for num in fr}

print(last_dig)