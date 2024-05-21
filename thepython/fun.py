def cal(a,b,operator):
    if operator == '+':
        print(f"the sum is {a+b}")
        f = input("enter Q for quit:")
        final(f)
    if operator == '-':
        print(f"the diff is {a-b}")
        f = input("enter Q for quit:")
        final(f)
    if operator == '*':
        print(f"the mul is {a*b}")
        f = input("enter Q for quit:")
        final(f)
    if operator == '%':
        print(f"the modulo is {a%b}")
        f = input("enter Q for quit:")
        final(f)
def final(quit):
    if quit.upper() == 'Q':
        exit()
    else:
        a, b, op= take_input()
        cal(a, b, op)

def take_input():
    try:
        a = int(input("enter num1:"))
        b = int(input("enter num1:"))
        op = input("enter your operator:")
    except Exception as e:
        raise e
    return a, b, op
    