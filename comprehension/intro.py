arr = [1, 2, 3, 4, 5, 6, 8, 9]

cubes = [num ** 3 for num in arr] # easy way to create list,tuple,set,dict from a sequence

print(cubes)

even_num = [num for num in arr if num % 2 == 0]

print(even_num)

odd_num = [num for num in arr if num % 2 != 0]

print(odd_num)

num_gt_five = [num for num in arr if num > 5]

print(num_gt_five)