number = int(input("Enter number: "))

count = 0

while number != 0 :
    digit = number % 10
    count += 1
    number //= 10

print(f"Total number of digits = {count}")