num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))

try:
    result = num1 / num2
    print(result)
except:
    num2 = int(input("Enter number 2 : "))
    result = num1 / num2
    print(result)
finally:
    print("Send text message....")
