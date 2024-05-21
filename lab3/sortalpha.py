#to sort string alphabetically
def sortalphabet(string):
    list = string.split("-")
    a = len(list)
    print(a)
    for i in range(len(list)):
        print(i)
        for j in range(0,len(list)-1-i):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
    print(list)
string = (input("enter the string: " ))
print(string)
sortalphabet(string) 