def fun1(*args):
    # print(args)
    sum = 0
    mul = 1
    for i in args:
        sum+=i
        mul*=i
    return sum,mul

