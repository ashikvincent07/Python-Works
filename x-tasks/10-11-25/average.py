def average_list(numbers):

    sum = 0

    for num in numbers:
        sum += num

    average = round(sum / len(numbers),1)

    return average

print(average_list([1, 2, 3, 4]))