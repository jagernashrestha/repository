# from pc3 import fun1
# fun1(5,6,7)
# # a,_,c = fun1(10,20,30)

# d1 = {"name":"ram"}
# print(d1["name "])
# print(d1.get("nam"))#terminatw na bhaye none return garxa
# print(d1.get("name"))

# n = int(input("enter the number:"))
# product = 1
# print("the product is")
# for i in range(1,11):
#     product = n*i
#     print(n ,"*", i ,"=",product)

# try:
#     c = 20
#     print(n)
#     raise Exception("ultopalto")
# except TypeError:
#     print("excpetion occured")

# except Exception as exe:
#     print(exe)
# finally:
#     print("out of loop")

class Student:
    def __init__(self,name):
        print("ja")
        self.name = name
        print(name)
obj = Student('jagga')

