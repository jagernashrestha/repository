#python program to check primr number
num1 = int(input(" enter the number "))
for i in range(2, num1):
    print(i)
    if num1%i == 0:
        print("number is common number")
        break
    else:
        print("number is prime")
        break




