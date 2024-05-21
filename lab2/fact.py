#factorial of number
try:
    n1 = int(input("enter the number"))
    fact = 1
    if n1>0:
        for i in range(1, n1+1):
            fact=fact*i
        print(f'factorial of number is:{fact}')
    else:
        print("cannot calculate the factorial")
except ValueError as n:
    print(n)
except TypeError as e:
    print(e)
except NameError as j:
    print(j)
except IndexError as d:
    print(d)
except ValueError as g:
    print(g)
except ValueError as h:
    print(h)
except Exception as v:
    print(v)
