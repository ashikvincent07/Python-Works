def common_divisor(num) :
    common_div = []

    for i in range(1, num+1):
        
        if num % i == 0:
            common_div.append(i)

    return common_div
        
print(common_divisor(8))