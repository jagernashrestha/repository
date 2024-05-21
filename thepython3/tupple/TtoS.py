#convert tuple into string
t1 = (20, 10, 1, 30)
str1 =  ""
for i in t1:
    if isinstance(i, str):
        str1+=i
    else:
        str1+=str(i)
print (str1)
# str2 = ''.join(str(t1))
# print(str2)