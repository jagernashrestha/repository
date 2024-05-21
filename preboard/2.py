# class Student():
#     def __init__(self):
#         self.roll = (input("entrt roll:"))
#         self.name = input("enter name:")
#         self.python_mark= int(input("Enter python mark:"))
#         self.maths_mark= int(input("Enter maths mark:"))
#         self.max_mark = 100
#     def total_mark(self):
#         self.total_marks = self.python_mark + self.maths_mark
#         return( self.total_marks)
#     def __str__(self):
#         return( self.name)
# obj1 = Student()
# a=obj1.total_mark()
# print(a)
# print(obj1)
    
# class animal:
#     def __init__(self, name):
#         self.name = name
#     # def __str__(self):
#     #     return "Its %s" % (self.name)
    
#     def __str__(self):
#         return self.name
# obj = animal('pogo')
# print(obj)
# print(obj.name)

# import numpy as np
# a1 = np.arange(0,10)
# print(a1)

# import numpy as np
# a1 = np.arange(0,100)
# a1.reshape(10,10)
# print(a1)

# np.argmax(a1)
# np.argmin(a1)

# r1 = np.random.radint(1,9,(3,3))
# r2 = np.random.radint(5,8,(3,3))
# np.add(r1 ,r2)
# np.multiply(r1,r2)
# r1/r2
# # rememberrrrrrrrrr toooo printttttt
# print(np.log(r1))
# print(np.exp(r2))
# print(np.log10(r1))
# print(np.mean(r2))
# print(np.median(r1))
# print(np.std(r1))
# print(np.corrcoef(r1))


#acending and decending without usinng builtin method

# def asc_dec():
#     num = []
#     n = int(input("enter the number:"))
#     for i in range(0,n+1):
#         num.append(i)
#         if num [i]> 999:
#             [i]+=[i+1,-i-1]
#     print(num)
# asc_dec()

# def sort_list(lst, ascending=True):
#     n = len(lst)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if ascending:
#                 if lst[j] > lst[j+1]:
#                     lst[j], lst[j+1] = lst[j+1], lst[j]
#             else:
#                 if lst[j] < lst[j+1]:
#                     lst[j], lst[j+1] = lst[j+1], lst[j]
#     return lst

# # Example usage:
# my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# sorted_ascending = sort_list(my_list)
# # sorted_descending = sort_list(my_list, ascending=False)

# print("Original List:", my_list)
# print("Sorted in Ascending Order:", sorted_ascending)
# # print("Sorted in Descending Order:", sorted_descending)


# def gcd(a, b):
#     """Function to find the greatest common divisor (GCD) using Euclid's algorithm."""
#     while b:
#         a, b = b, a % b
#     return a

# def lcm(a, b):
#     """Function to find the least common multiple (LCM) of two numbers."""
#     return (a * b) // gcd(a, b)

# # Example usage:
# num1 = 12
# num2 = 18
# print("Least Common Multiple of", num1, "and", num2, "is:", lcm(num1, num2))


# def gcd(a,b):
#     while b:
#         a,b = b, a%b
#     return a
# def lcm(a,b):
#     return(a*b)//gcd(a,b)
# n1 = 10
# n2 = 20
# print(lcm(n1,n2))

# def add(a=1,b=2):
    
#     c = a + b
#     d = a-b
#     return c,d
# e = (add())
# print(e[1])

# def  fun1(normal_arg, *args, **kwargs): 
#     print(normal_arg)
#     print(*args)
#     # print(**kwargs["name"])
# fun1("ram", 10, 30, 40, name="hari",address ="itahari") 
# # fun1(1,2,3,"ram",name="ktm")


# def factoria(n):
#     """Recursive function to calculate the factorial of a non-negative integer."""
#     # Base case: factorial of 0 is 1
#     if n == 0:
#         return 1
#     # Recursive case: n * factorial(n-1)
#     else:
#         return n * factoria(n - 1)

# # Example usage:
# numbe = 5
# print("Factorial of", numbe, "is:", factoria(numbe))

# d1 = {"name":"ram", "address":"ktm", "roll":20} 
# print(d1) 

# dict1 = {"name": "ram", "address": "ktm"} 
# # Adding a new key-value pair 
# dict1["age"]  = 20 

# my_list = [1, 2, 3, 4, 25] 
# for item in my_list: 
#     print(item) 

# l1 = [1, 2, "ram", "hari"] 
# length = len(l1) 
# try: 
#     print(l1[length]) 
# except IndexError: 
#     print("Index out of range") 
# except Exception as exe: 
#     print(exe) 

# for i in range(5): 
#     if i == 3: 
#         continue  # Skip the rest of the loop for i=3 
#     else: 
#         print(i) 

# # Example: 
# num = [10, 20, 30, 40,50,80] 
# for i in num: 
#     if i == 50: 
#         print(f'The loop has been break with value{i}') 
#         break 
#     else: 
#         print(f"running loop.") 
# print('Outside the for loop.') 

# i = 0 
# while i <= 2: 
#     j = 0 
#     while j <= 2: 
#         print(i, j) 
#         j += 1 
#     i += 1 