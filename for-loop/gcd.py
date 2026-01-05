num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))

small_num = min(num1, num2)

gcd = 0

for i in range(1, small_num+1) :
    
    if num1 % i == 0 and num2 % i == 0 :
        gcd = i

print(f"GCD = {gcd}") 