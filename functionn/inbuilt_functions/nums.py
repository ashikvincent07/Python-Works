nums = [23, 3, 4, 6, 2, 9]

square = list(map(lambda n: n ** 2, nums))
cube = list(map(lambda n: n ** 3, nums))
add_five = list(map(lambda n: n + 5, nums))


print(square)
print(cube)
print(add_five)


even = list(filter(lambda n: n % 2 == 0, nums)) # filter only returns condition true elements
print(even)

odd = list(filter(lambda n: n % 2 != 0,nums))
print(odd)

num_gt_five = list(filter(lambda n: n > 5, nums))
print(num_gt_five)

