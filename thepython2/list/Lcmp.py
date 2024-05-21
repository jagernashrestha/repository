list1 = ['ab','aba','bca','cdc']
count = 0
for i in list1:
    if len(list1)>1 and i[0] == i[-1]:
        count+=1
print(count)