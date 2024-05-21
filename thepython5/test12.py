try:
    def fun1( *args):
        args = args[0]
        sum  = 0
        for i in args:
            sum+=i
        return sum
    num = int(input("enter the number:"))
    g = []
    for i in range(1, num+1):
        i = int(input(f'enter the{i}number '))
        g.append(i)
    total = fun1(g)
    print(total ,end=' ')

except ValueError as n:
    print (n)
    