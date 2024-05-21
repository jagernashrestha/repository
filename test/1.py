def sort_fun(num):
    for i in num:
        print(i)
        if num[i] > num[i+1]:
            num[i], num[i+1] = num[i+1], num[i]
    print(l1)
        # return num
l1 = [10,20,80,2,5,6]
sort_fun(l1)

# # def bubble_sort(numbers):
# #     n = len(numbers)
    
# #     # Traverse through all array elements
# #     for i in range(n):
# #         # Last i elements are already in place, so we reduce the range
# #         for j in range(0, n-i-1):
# #             # Traverse the array from 0 to n-i-1
# #             # Swap if the element found is greater than the next element
# #             if numbers[j] > numbers[j+1]:
# #                 numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

# #     return numbers
# # bubble_sort(   )
# def bubble_sort(numbers):
#     n = len(numbers)
    
#     # Traverse through all array elements
#     for i in range(n):
#         # Last i elements are already in place, so we reduce the range
#         for j in range(0, n-i-1):
#             # Traverse the array from 0 to n-i-1
#             # Swap if the element found is greater than the next element
#             if numbers[j] > numbers[j+1]:
#                 numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

#     return numbers
# numbers = 1,20,30,4,5
# bubble_sort(numbers)

# no1 = [2,3,4,5]
# comprehension = [i**2 for i in no1]
# print("Comprehension: ", comprehension)

# def factorial(num):
#     fact = 1
#     for i in range(1,num+1):
#         fact*=i
#     print(fact)
# num = int(input('enter the number:'))
# factorial(num)

# # # fibonacci series
# number = 0
# num2 = 1
# list1 = []

# no = int(input("enter a number:"))
# if no == 1:
#     print(number)
# elif no == 2:
#     print(number, num2)
# else:
#     list1 = [number]
#     for i in range(1,no):
#         list1.append(num2 )
#         number,num2 = num2,number+num2
#     print(list1)
    