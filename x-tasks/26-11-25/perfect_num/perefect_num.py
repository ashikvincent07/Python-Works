file_path = "x-tasks/26-11-25/perfect_num/numbers.txt"

fr = open(file_path, "r")

perfect_num = []
# nums = [int(line.rstrip("\n")) for line in fr]

for num in fr:
    number = int(num.rstrip("\n"))
    sum = 0
    for i in range(1, number):
        if number % i == 0:
            sum += i

    if sum == number:
        perfect_num.append(number)

print(perfect_num)
