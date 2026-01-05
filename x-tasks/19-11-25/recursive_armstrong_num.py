numbers = [150,151,153,148,153,16341,1700,16341,153]

armstrong_num = []

for num in numbers:
    digit = 0
    temp = num
    sum = 0
    num_of_digits = 0

    while temp != 0:
        num_of_digits += 1
        temp //= 10

    temp = num

    while temp != 0:
        digit = temp % 10
        sum += digit ** num_of_digits
        temp //= 10

    if sum == num :
        armstrong_num.append(num)

armstrong_num_count = {}

for num in armstrong_num:

    if num in armstrong_num_count:
        armstrong_num_count[num] += 1

    else:
        armstrong_num_count[num] = 1

recursive_armstrong_num = {k for k, v in armstrong_num_count.items() if v > 1}

print(recursive_armstrong_num)



    


