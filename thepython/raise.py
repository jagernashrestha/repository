age= int(input("enter the age:"))
try:
    if age<16:
        raise Exception("You are a child.")
    print("greater than 16")
except TypeError as exception:
    raise exception
