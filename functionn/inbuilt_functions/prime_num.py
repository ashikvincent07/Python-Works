number = 12

print(not any(number % i == 0 for i in range(2, int(number/2)+1)))