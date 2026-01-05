number = int(input("Enter number: "))

is_prime = True

for i in range(2, number):

    if number % i == 0:
        is_prime = False

        break

result = "Prime Number" if is_prime else "Not Prime Number"

print(result)