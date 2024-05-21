try:
    def prime(l):
        prime = []
        notprime = []
        for i in l:
            is_prime = True
            for j in range(2,i):
                if i % j == 0:
                    is_prime=False
                    break
                
            print(is_prime, i)
            if is_prime  == True :
                prime.append(i)
            else :
                notprime.append(i)
            is_prime = True

        print(prime,notprime)
    l1  = [2, 3, 5 , 8 , 10 , 15]
    prime(l1)
except TypeError as t :
    print(t)
except ValueError as v:
    print(v)
except IndexError as i:
    print("Index Error", i)
except Exception as h  :
    print(h)