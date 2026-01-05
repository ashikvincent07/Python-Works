lst = [10, 20, 30, 40]

dict_lst = {num : num ** index for index, num in enumerate(lst, 1)}

print(dict_lst)