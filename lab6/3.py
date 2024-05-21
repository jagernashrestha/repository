# 3,Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.



try:
    num1 = int(input("enter num1:"))
    num2 = int(input("enter num2:"))
    result = num1 / num2
    print(result)
except Exception as d:
    print(" ZeroDivisionError")
