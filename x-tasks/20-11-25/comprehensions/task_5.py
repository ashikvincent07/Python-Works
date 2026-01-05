cube_of_num_div_by_3_from_1_to_30 = [
    (num, num ** 3) for num in range(1, 31) if num % 3 == 0
]


print(cube_of_num_div_by_3_from_1_to_30)