try:
    def f1(a1,a2):
        print(a1,a2)
        print(a1.upper(),a2.upper())
    a1 = input("enter the string1:")
    a2 = input("enter the string2:")
    f1(a1,a2)
except TypeError as n:
    print(n)