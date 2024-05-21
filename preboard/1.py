# #check nnnumber is positive or negative or zero

# n = int(input("enter the number:"))
# if n>0:
#     print("number is positive")
# elif n<0:
#     print("number is negative")
# else:
#     print("the number is zero")


# #maximum of 3 number
# n1=int(input("Enter first number:"))
# n2=int(input("Enter second number:"))
# n3=int(input("Enter third number:"))    

# if(n1>n2) and(n1>n3):
#     print(n1, "is greater")
# elif(n2>n1) and (n2>n3):
#     print(n2,"is greater")
# else:
#     print(n3,"is greater")

# #if ther year is leap year
# year = int(input("enter the year:"))
# if((year % 4 == 0)
#     and (year % 100 != 0)
#     or (year % 400 == 0)):       
#     print("leap year")
# else:
#     print("not a leap year") 
# n = int(input("enter the  num"))
# if (n%4 ==0)and (n%400==0)and (n%100!=0 ):
#     print ("The year is Leap Year")
# else:
#     print("not a leap year")

# #even or odd
# n = int(input("enter the number"))
# if n%2!=0:
#     print("the number is odd")
# else:
#     print("even")

# #to find roots of quadratic equation
# a=float(input("enter the number:"))
# b=float(input("enter the value of b:"))
# c=float(input("enter the value of c:"))

# print(complex((-b+(b**2-4*a*c)**0.5)/2*a ))
# print(complex((-b-(b**2-4*a*c)**0.5)/2*a))

# #check prime or not
# num = int(input('Enter a number :'))
# count = 0
# for i in range(1, num):
#     if num % i == 0:
#         count += 1
# if count > 1:
#     print(f"{num} is a composite number.")
# else:
#     print(f"{num} is a prime number.")

# #palindrome
# a = input("entre thw num:")
# rev = a[::-1]
# if a == rev:
#     print("it's palindrome")
# else:
#     print("it's not palindrome")

# #factorial of number
# n = int(input("Enter the number: "))
# fact = 1
# for i in range(1,n+1):
#     print(i)
#     fact = i*fact
# print("The factorial of", n,"is: ",fact)

# #fibonacci series
# n = int(input("enter t
# he n of terms:"))
# count1,count2 = 0,1
# print("Fibonacci Series: ")
# for i in range(n):
#     print(i)
#     print(count1)
#     fn = count1 + count2
#     count1 = count2
#     count2 = fn

#file
# f = open("demo.txt","r

# f1 = open(" file1.txt","r")
# print(f1.read())
# f1.close()


# f1 = open(" file1.txt","w")
# f1.write("Hello World!")
# f1.close()
# f1 = open(" file1.txt","r")
# print(f1.read())
# f1.count()
# f1.close()
# with open ("file1.txt","w")as f:
#     (f.write("hello "))

# with open ("file1.txt","r")as f:
#     print(f.read())
# with open('filename.txt', 'r') as file: 
# # Read the entire contents of the file 
# file_content = file.read() 
# print(file_content)
# try:  
#     def function ():
#         with open('file.txt', 'r') as f: 
#             count = 0
#             lines = f.readlines() 
#             for line in lines: 
#                 count = count+1
#             return(count)
#     a = function()
#     print(a)
# except FileNotFoundError:
#     print("The specified file was not found.") 


# try:
#     name = input("enter thename of file:")
#     name = name+".txt"
#     if name ==  "file1.txt":
#         print("File opened successfully")
#     else:
#         raise ValueError("This is an error")
        
#     with open ("file2.txt","r")as f:
#         f.read()
# except FileNotFoundError:
#     print("error")

# def read_file(filename):
#     try:
#         with open(filename, 'r') as file:
#             contents = file.read()
#             print(contents)
#     except FileNotFoundError:
#         print("File not found. Please enter a valid filename.")
#         return False
#     return True
# while True:
#     filename = input("Enter a filename: ")
#     if read_file(filename):
#         break

# def is_armstrong(num):
#     # Convert number to string to iterate through digits
#     name = str(num)
#     # Calculate the number of digits
#     digits = len(name)
#     # Initialize sum
#     sum = 0
    
#     # Iterate through digits and calculate the sum of each digit raised to the power of digits
#     for digit in name:
#         sum += int(digit) ** digits
    
#     # Check if the sum equals the original number
#     return sum == num

# # Test the function
# number = int(input("Enter a number to check if it's an Armstrong number: "))
# if is_armstrong(number):
#     print(number, "is an Armstrong number.")
# else:
#     print(number, "is not an Armstrong number.")

# class circle():
#     def  __init__(self):
#         self.radius = int(input("entrt the radius of circcle:"))
#     def area(self):
#         area = 3.14*self.radius**2
#         return area
#     def perimeter(self):
#         perimeter = 2*  3.14* self.radius
#         return perimeter
# obj = circle()
# print(obj.area())
# print(obj.perimeter())

# class person():
#     def __init__(self):
#         self.name = input("enter the name:")
#         self.country = (input("enter the country:"))
#         self.birthyear = int (input("enter the birth year:"))
#     def age(self):
#         current_year = 2024
#         age = current_year- self.birthyear
#         return age
    
# obj = person()
# print(obj.age())

# class vechicle():
#     def drive(self):
#         print("welcome to class vechicle")

# class car(vechicle):
#     def drive(self):
#         print("you can drive  your car")
#         super().drive ()
# class  bike(vechicle):
#     def drive(self):
#         print("you are riding your bike ")
# obj1 = car()
# obj2 = bike()
# print(obj1.drive())
# print(obj2.drive())

# class Vehicle:
#     # def __init__(self):
#     #     self.color = "Black"
#     def drive(self):
#         print("you can drive vechicle")
# class Bicycle(Vehicle):
#     def drive(self):
#         print("you can ride a bicycle")
#         super().drive()
# class Car(Vehicle):
#     def drive(self):
#         print("you can drive a car")
# obj1 = Car()
# obj2 = Bicycle()
# obj1.drive()
# obj2.drive() 

# #create 1d array
# n = int(input ("enter the number:"))
# arr = []
# for i in range (0, n) :
#     ele = int(input("Enter element of array:"))
#     arr.append(ele)
# print ("Array is:", end=" ")
# for i in range (0, n) :
#     print("%d" %arr[i],end=" ")

# #create 3d array
#     r=int(input("Enter no.of rows:"))
#     c=int(input("Enter no.of columns:"))
#     M=[]
#     for i in range(0,r):
#         T=[]
#         for j in range(0,c):
#             x=(i*j)%5   

# class atm():
#     def __init__(self):
#         self.balance=1000
#         self.name = input("Enter your name:")
#         self.account_no = int( input("Enter account number:"))
#         self.address = input("enter the address:")
#         self.current_balance = self.balance
#         self.menu()

#     def menu(self):
#         num = (input("""
#                 1.users details
#                 2.check balance
#                 3.withdrawl amt
#                 4.deposit amt
#             """))
#         if num == "1":
#             self.user_details()
#         if (num == "2"):
#             self.check_balance()

#         if (num == "3"):
#             self.withdrawal()

#         if (num == "4"):
#             self.deposit_amt()
#         else:
#             exit()
#     def check_balance(self):
#         print(self.current_balance,"is your current balance.")
#         self.menu()
#     def deposit_amt(self):
#         self.deposit = int(input("Deposite amount:"))       
#         self.current_balance = self.balance+ self.deposit
#         print (self.current_balance,"Your current balance is Rs.")
#         self.menu()

#     def withdrawal(self):
        
#         self.withdrawal = int(input("enter the amt to be withdrawl:"))
#         if (self.current_balance >=self.withdrawal):
#             self.current_balance -= self.withdrawal
#             print ("Amount Withdrawn Successfully")
#         else:
#             print( "Insufficient Balance")
#         print("Your Current Balance is Rs.",self.current_balance)
#         self.menu()
#     def user_details(self):
#         print(self.name)
#         print(self.address)
#         print(self.account_no)
#         print(self.current_balance)
#         self.menu()

        
# obj = atm()

