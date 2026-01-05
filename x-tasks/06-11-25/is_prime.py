def is_prime_num(num):
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    return is_prime

print(is_prime_num(73))