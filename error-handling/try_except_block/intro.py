# try : doubtfull code, except: handling code if erro occurs, finally: always executes 

n1 = int(input("Enter number 1 : "))
n2 = int(input("Enter number 2 : "))

try:
    result = n1/n2
    print(result)

except Exception as e:
    print(e)

print(n1,n2)