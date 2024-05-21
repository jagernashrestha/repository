l1 = [10,20,80,2,5,6]
for i in l1:
    if l1[i] > l1[i+1]:
            l1[i], l1[i+1] = l1[i+1], l1[i]
    print(l1)