from functools import reduce

lst = [1, 2, 5, 3, 10, 7]

max_num = reduce(lambda n1, n2: n1 if n1 > n2 else n2, lst)
# print(max_num)

min_num =reduce(lambda n1, n2: n1 if n1 < n2 else n2, lst)
# print(min_num)

product = reduce(lambda n1, n2:n1 * n2, lst)
# print(product)


num_gt_five = [n > 5 for n in lst]
is_all_gt_five = all(num_gt_five)  # retrun true if all elements are true
print(is_all_gt_five)