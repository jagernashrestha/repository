#factorial using function
def fact():
    num = int(input("enter the number:"))
    if num>0:
        fact = 1
        for i in range(1,num+1):
            fact*=i
        print(fact)
    else:
        print("enter the postitive number")
    
#calling the function with number
fact()