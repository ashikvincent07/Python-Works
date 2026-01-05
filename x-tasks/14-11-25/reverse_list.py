fruits = ["apple", "banana", "cherry", "apple"]

reverse_list = []

length = len(fruits)

for i in range(length-1, -1, -1):
    reverse_list.append(fruits[i])

print(reverse_list)
