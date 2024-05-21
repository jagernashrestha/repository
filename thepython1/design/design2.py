# print design

for i in range(1,7):
    # print(i)
    for j in range(1,1+i):
        # print(i,j)
        print("*",end=' ')
    print('')
for i in range(1,7):
    # print(i)
    for j in range(1,7-i):
        # print(j)
        print("*",end=' ')
    print('')