# #inheritance->single, nultiple,multilevel,hiearchial,hybrid
##single inheritance
# class animal:
#     def function1(name):
#         # print(name)
#         print("function1 successful")
# class Dog(animal):
#     def bird(self):
#         print("parrot")
# obj = Dog()
# obj.bird()
# obj.function1()

# class Student:
#     def Roll(self):#yo chai aauta method ho
#         print("06")
# class Result(Student):
#     def Exam(self):
#         print('A+')
# object = Result()
# object.Roll()
# object.Exam()
##multiple inheritanceee
# class Student:
#     def Roll(self):#yo chai aauta method ho
#         print("06")
# class Name:
#     def enter_name(self):
#         print("Jagerna Shrestha")
# class Result(Student,Name):
#     def Exam(self):
#         print('A+')
# object = Result()
# object.enter_name()
# object.Roll()
# object.Exam()
# ##multilevel inheritance
# class Student:
#     def Roll(self):#yo chai aauta method ho
#         print("06")
# class Name(Student):
#     def enter_name(self):
#         print("Jagerna Shrestha")
# class Result(Name):
#     def Exam(self):
#         print('A+')
# object = Result()
# object.enter_name()
# object.Roll()
# object.Exam()

###Hiearchial inheritance
# class Student:
#     def Roll(self):#yo chai aauta method ho
#         print("06")
# class Name(Student):
#     def enter_name(self):
#         print("Jagerna Shrestha")
# class Result(Student):
#     def Exam(self):
#         print('A+')
# object1 = Name()
# object2 = Result()
# object1.enter_name()
# object1.Roll()
# object2.Roll()
# object2.Exam()