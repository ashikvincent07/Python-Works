number = int(input("Enter number: "))

even_sum = 0

for i in range(2, number+1, 2):
    even_sum += i

print(f"Sum of even numbers upto {number} = {even_sum}")