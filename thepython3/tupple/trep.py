# replace last value of tupple in list
t1= [(8,9),(9,7),(5,4)]
l1 = []
for i in t1:
    l2 = list(i)
    l2.remove(l2[-1])
    l1.append(tuple(l2))
print (l1) 