
#FIND OUTPUT OF POWERS
num1 = int(input("enter the number"))
num2 = int(input("enter the number"))
num3 = int(input("enter the number"))
if (num1>num2>num3):
    print(f'{num1}is greater than other')
if (num2>num1>num3):
    print(f'{num2}is greater than other')
if (num3>num2>num1):
    print(f'{num3}is greater than other')