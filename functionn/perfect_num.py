def perfect_num(num):

    sum = 0

    for i in range(1, num):

        if num % i == 0:
            sum += i
    
    result = "Perfect Number" if num == sum else "Not a Perfect Number"

    return result
    
print(perfect_num(28))