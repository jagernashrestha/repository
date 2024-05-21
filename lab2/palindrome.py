#palindrom number
num =input("enter the number:")
num1 = num [::-1]
if num == num1:
    print("palindrom")
else:
    print("num is not palindrom")