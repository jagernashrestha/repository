def fun1(a,*args,**kwargs):
    for key,value in kwargs.items() :
        print(key +":" +value)
    print(a)
    print(*args)
    print(kwargs)
    sum = 0
    for i in args:
        sum+=i
    print(sum)
if __name__ =="__main__":
    fun1(0,1,2,3,name = "don", address = "ktm")

