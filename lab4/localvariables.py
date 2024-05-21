def local_variables():
    x = 10
    y = "Hello"
    z = True
print(local_variables.__code__.co_nlocals)