def gcd(num1, num2):
    gcd_two_num = 1
    min_num = min(num1, num2)

    for i in range(2, min_num+1):

        if num1 % i == 0 and num2 % i == 0:
            gcd_two_num = i

    return gcd_two_num


print(gcd(1,4))