
def even(l1):
    sum = 0
    for i in l1:
        if i%2 ==0:
            sum +=i
    print("sum of even numbers:" ,sum)
l1 = [1,2,3,4,5,6,8,9,7,0]
even(l1)         

