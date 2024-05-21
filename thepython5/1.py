try:
    def funa(l1):
        prime = []
        common_num = []
        for i in n:
            n = int(input("enter the num:"))
            for j in range(1,n+1):
                if n % i == 0 :
                    prime.append(i)
                else :
                    common_num.append(i)
        print(prime)     
except TypeError as n:
    print(n)