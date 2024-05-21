try:
    def fun1(a):
        less = a[0]
        for i in a:
            i<less
            less = i
        return less
    l1 = [10,12,9,6,5]
    min = fun1(l1)
    print(min)
    fun1(l1)

except TypeError as n:
    print(n)