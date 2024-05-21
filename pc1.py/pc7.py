# try:
#     class Homosapiens:
#         def show(self):
#             print("welcome to homosapiens")

#     class Person:
#         def show(self) :
#             print("welcome to classs person")
        
#     class Employee(Person , Homosapiens):
#         def show(self):
#             print("welcome to class employee")

#     class Ram(Person):
#         def show(self):
#             print("hello raam")
    
#     obj1 = Employee()
#     obj1.show()
#     obj2 = Ram()
#     obj2.Ram()

# except Exception as exe:
#     print(exe)
# ako thiye tme guff garfai thiyau
try:
    class Homosapiens:
        def show(self):
            print("welcome to homosapiens")

    class Person(Homosapiens):
        def show(self) :
            print("welcome to classs person")
            super().show()

    class Employee(Homosapiens):
        def show(self):
            print("welcome to class employee")
            super().show()
    obj1 = Employee()
    obj1.show()
except Exception as exe:
    print(exe)





