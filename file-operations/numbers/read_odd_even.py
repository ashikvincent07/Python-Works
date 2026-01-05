file_path = "file-operations/numbers/numbers.txt"

fr = open(file_path, "r")

nums = [int(line.rstrip("\n")) for line in fr]

even_num = [num for num in nums if num % 2 == 0]

odd_num = [num for num in nums if num % 2 != 0] 

print(odd_num)

print(even_num)