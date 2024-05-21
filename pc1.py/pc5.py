# class Atm:
#     __bank = "siddhartha bank limited"
#     __hello = "hello aajja"
#     def __init__(self,name) :
#         self.name  = name
#     def showage(self,age):
#         print("bank name:",Atm.__bank  )
#         print("who is  she",Atm.__hello)
#         print(f"my name is {self.name} and age is {age}")
#     def __str__(self):
#         # return("aajaa")
#         return(f"{self.name}")
#     def amoount(self):
#         self.enter
# obj1 = Atm("ram")
# obj2 = Atm("ajja")
# obj1.showage(10)
# print(obj1)#adress print hunxa 
# l1 = [10,20,30]
# print(l1)#value print hunxa

# try:
#     class Calculator:
#         def __init__(self, *args):
#             self.num1 = int(input('Enter first number: '))
#             self.num2 = int(input('Enter second number: '))
#             Calculator.menu(self)
#         def menu(self):
#             print("\nChoose an operation to perform below: ")
#             num = int(input("enter the number:"))
#             '''
#             1.additionn
#             2.substraction
#             3.multiplication
#             4.division'''
#             if (num == 1):
#                 Calculator.addition(self)
#             elif(num==2):
#                 Calculator.subtraction(self)
#             elif(num==3):
#                 Calculator.multiply(self)
#             else:
#                 Calculator.division(self)
#         def addition(self):
#             print(self.num1+self.num2)
#             Calculator.menu(self)
#         def substraction(self):
#             print(self.num1-self.num2)
#             Calculator.menu(self)
#         def multiplication(self):
#             print(self.num1*self.num2)
#             Calculator.menu(self)
#         def  division(self):
#             if self.num2==0:
#                 print("Error! Division by zero is not allowed.")
#             else:
#                 print(f"{self.num1}/{self.num2}={self.num1/self.num2}") 
#             Calculator.menu(self)
#     c=Calculator()    
# except ValueError:
#     print("Invalid input! Please enter a valid integer.")
# except Exception as exe:
#     print(exe)


# class Calculator:
#     try:
        
#         def __init__(self):
#             self.menu(self)
#         def menu(self):
#             self.num1 = int(input('Enter first number: '))
#             self.num2 = int(input('Enter second number: '))
#             print("\nChoose an operation to perform below: ")
#             print('''
#             1.additionn
#             2.substraction
#             3.multiplication
#             4.division''')
#             num = int(input("enter the number:"))
#             if (num == 1):
#                 self.addition(self)
#             elif(num==2):
#                 self.substraction(self)
#             elif(num==3):
#                 self.multiplication(self)
#             else:
#                 self.division(self)
#         def addition(self):
#             print(self.num1+self.num2)
#             self.menu(self)
#         def substraction(self):
#             print(self.num1-self.num2)
#             self.menu(self)
#         def multiplication(self):
#             print(self.num1*self.num2)
#             self.menu(self)
#         def  division(self):
#             if self.num2==0:
#                 print("Error! Division by zero is not allowed.")
#             else:
#                 print(f"{self.num1}/{self.num2}={self.num1/self.num2}") 
#             self.menu(self)
# c =    Calculator()   
#     except ValueError:
#         print("Invalid input! Please enter a valid integer.")
#         c.menu()
#     except Exception as exe:
#         print(exe)
#         c.menu()

#     c.menu()    
