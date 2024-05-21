# 4, Write a Python program to handle a custom exception when user input age is than less 16.
age= int(input("enter the age:"))
try:
    if age<16:
        raise Exception("You are a child.")
    print("greater than 16")
except Exception as exception:
    print (exception)