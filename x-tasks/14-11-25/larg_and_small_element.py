numbers = [10, 20, 30, 40, 50]

largest_element = numbers[0]

smallest_element = numbers[0]

for num in numbers:
    
    if num >= largest_element:
        largest_element = num

    if num < smallest_element:
        smallest_element = num

print(f"Smallest element : {smallest_element}\nLargest element {largest_element}")