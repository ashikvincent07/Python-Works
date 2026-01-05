def factorial(num):
    fact = 1
    for i in range(1, num+1):
        fact *= i
    return fact

dict_factorial_1_to_10 = {num : factorial(num) for num in range(1, 11)}

print(dict_factorial_1_to_10)