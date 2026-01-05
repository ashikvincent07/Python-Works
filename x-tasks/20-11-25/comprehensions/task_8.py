nested_list =  [[1,2], [3,4], [5,6]]

output = [c for r in nested_list for c in r]

print(output)