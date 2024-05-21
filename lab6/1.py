# 1,Create a Parent class called  Vehicle with a method called drive and 
# create class called Car and Bicycle that inherit from Vehicle and override the drive method.
class Vehicle:
    # def __init__(self):
    #     self.color = "Black"
    def drive(self):
        print("you can drive vechicle")
class Bicycle(Vehicle):
    def drive(self):
        print("you can ride a bicycle")
        super().drive()
class Car(Vehicle):
    def drive(self):
        print("you can drive a car")
obj1 = Car()
obj2 = Bicycle()
obj1.drive()
obj2.drive() 

# class vechicle:
#     def drive (self):
#         print("you can drive a vechicle")

# class bike(vechicle):
#     def drive (self):
#         print("you can ride bike")
# class  car(vechicle):
#     def drive (self):
#         super().drive()
#         print("you can drive")
# a= car()
# b=bike()
# a.drive()
# b.drive()