file_path = "file-operations/numbers/numbers.txt"

fr = open(file_path, "r")

reverse_num = [int(num[::-1]) for num in fr]

print(reverse_num)

