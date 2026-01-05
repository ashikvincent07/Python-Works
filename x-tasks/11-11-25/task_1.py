arr = [1, 5, 7, 9, 12, 15, 16, 19, 20]

odd_num_count = 0
even_num_count = 0

print("Even numbers: ",end=" ")

for num in arr:

    if num % 2 == 0:
        print(num,end=", ")
        even_num_count += 1

print(f"\nEven number count = {even_num_count}")

print("Odd numbers: ",end=" ")

for num in arr:

    if num % 2 != 0:
        print(num,end=", ")
        odd_num_count += 1

print(f"\nOdd numbers count = {odd_num_count}")