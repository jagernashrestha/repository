def f1(n1,n2,operator1):
    
    if operator1 == "+":
        return n1 + n2
    elif operator1 == "-":
        return  n1 - n2
    elif operator1 == "*":
        return  n1 * n2
    else:
        raise ValueError ('invalid operator ')
n1 = int(input("Enter the number:"))
n2 = int(input("Enter another number:"))
operator=input('Enter the operator (+,-,*,/):')
print(f"The result is {f1(n1,n2,operator)}")