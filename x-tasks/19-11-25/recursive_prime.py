numbers = [2,4,5,10,13,14,13,11,7,9,7]

def prime_num(numbers):
    prime_numbers = []

    for num in numbers:
        if num < 2:
            is_prime = False
            continue

        is_prime = True

        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            prime_numbers.append(num)

    return prime_numbers

prime_numbers = prime_num(numbers)

num_count = {}

for num in prime_numbers:

    if num in num_count:
        num_count[num] += 1
    
    else:
        num_count[num] = 1

recursive_prime = {k for k,v in num_count.items() if v > 1}

print(recursive_prime)


