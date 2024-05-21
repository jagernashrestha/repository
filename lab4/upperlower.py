def funcction1(string1):
    count1 = 0
    count2 = 0
    for i in string1:
        if i.isupper():
            count1+=1
            print(count1)
        else:
            count2+=1
            print(count2)
    print(count1,count2)
string1 = "Hi My Name Is Jagerna Shrestha"
funcction1(string1)