file_path = "error-handling/num/nums.txt"

fr = open(file_path, "r", encoding="utf-8")

nums = []

for line in fr:
    line = line.rstrip("\n")
    try:
        num = int(line)
        nums.append(num)
    except Exception as e:
        continue

print("All numbers: ",nums)

even_numbers = [num for num in nums if num % 2 == 0]

print("Even numbers: ",even_numbers)

even_num_count = {num : even_numbers.count(num) for num in set(even_numbers)}

print("Even number count: ",even_num_count)

max_count_even_num = [n for n, c in even_num_count.items() if c == max(even_num_count.values())]

print("Most frequent even num: ",max_count_even_num)
