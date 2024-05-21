try:
    
    def funa(l1):
        odd = []
        even = []
        for i in l1:
            if i %2 == 0:
                even.append(i)
            else :
                odd.append(i)
        print(odd,even)
    l = [20, 30, 12, 15, 32]
    funa(l)        
except TypeError as n:
    print(n)

