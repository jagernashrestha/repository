# txt = "The best things in life are free!"
# print("freee" in txt)
# b = "Hello, Worldo!"
# print(b[:5])
# print(b[2:])
# print(b[-5:-2])

# int i = 0; c 
# for(i=0;i<n;i++){
    
    
    
    
# }
# for i in range(1,5):
#     c+=1
#     print(c)
num=int(input('enter a number'))
div=int(input('enter a divisor'))
c = 0
while True:
    c+=1
    num =num-div
    
    if c == 3:
        break
print(f'quotient{c}')
print('remder is',num)

# def sorr(l1):
#     # l2  =[]
#     print(l1[0])
#     print(l1[1])
#     print(l1[2])
#     # for i in range(0,len(l1)) :
#     #     print(i)
#     #     if l1[i] >  l1[i+1]:
#     #         l1[i],l1[i+1] =l1[i+1],l1[i]
#     # print(l1)
# l1 = [1,2,7,6,4,0]
# sorr(l1)
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
#     print(numbers)
    
# numbers = [1,2,7,6,4,0]
# bubble_sort(numbers)

# num = [ i**2 for i in numbers]
# print(num)
#fibonanci series
# def fibo(n):
#     a ,b = 0,1
#     if n == 0:
#         print ([])
#     elif n==1:
#         print ([a])
#     else:
#         fib = [a]
#         print(a,end =",")
#         while len(fib)<n:
#             fib.append(b)
#             print(b,end=",")
#             a,b=b,a+b
#             # print(b)
#     # print(fib)
    
# fibo(5)