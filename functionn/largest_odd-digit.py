def largest_odd_digit(n):
    temp = 0
    digit = 0
    largest_odd = 0

    while n!= 0:
        temp = n
        
        if n % 2 != 0:
            return n
        
        else:
              
            digit = temp % 10
        
            if digit % 2 != 0 and digit > largest_odd:
                largest_odd = digit

            temp = temp // 10

            if temp % 2 != 0 and temp > largest_odd:
                largest_odd = temp

        if largest_odd != 0:
            return largest_odd
        
        else:
            return "No Odd number digits"
            
    

print(largest_odd_digit(1378))

            

