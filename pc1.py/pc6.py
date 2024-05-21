# #object call ,parameterized and non parameterized
# try:
#     class People():
#         def __init__(self,name,age):
#             self.__name = name
#             self.age = age
#         def setter(self,name):
#             self.__name = name
#         def show(self):
#             print(f'name is {self.__name} age is {self.age}')
#     obj1 = People("ram",10)
#     # obj2 = People("hari",30)
#     obj1.show() 
#     obj1.setter("bukkie")
#     # obj2.show()
#     # print(obj1.__name)
#     # obj1.name = "hari"
#     # obj1._People__name = "aaja"
#     obj1.show()

# except Exception as exe:
#     print(exe)

import math
class Circe:
    def __init__(self):
        self.radius = int(input("enter the radius:"))
    def area(self):
        area = round(math.pi *self.radius**2,3)
        print(area)
    def perimeter(self):
        perimeter = round(2*math.pi*self.radius,3)
        print(perimeter)
obj1 = Circe()
obj1.area()
obj1.perimeter()
