A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

common_elements = A.intersection(B)
print(f"Common elements = {common_elements}")

a_diff_b = A.difference(B)
print(f"Present in A and not in B = {a_diff_b}")

symetric_diff = A.symmetric_difference(B)
print(f"Symmetric difference = {symetric_diff}")