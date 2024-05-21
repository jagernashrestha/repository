#prime number
num = int(input('Enter the number '))
for i in range(2,num):
    if num% i == 0:
        #print(i)
        is_notprime = True
        break
    else :
        #print(i)
        is_notprime = False
if is_notprime == True :
    print('Entered num is not prime')
else :
    print(' prime')