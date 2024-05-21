try:
    def f1(a):
        less = 9999
        for i in a:
            i<less
            less = i
        print(less)
    l1 = [10,12,9,6,5]
    f1(l1)

except TypeError as n:
    print(n)  