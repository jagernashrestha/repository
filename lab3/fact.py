#factorial using function
def factorial1(a):
    fact = 1
    for i in range(1,a+1):
        fact*=i
    return(fact)
#calling the function with number
if  __name__ =="__main__":
    num = int(input("enter the number:"))
    if num>0:
        print(factorial1(num))
    else:
        print("enter the0 postitive number")