# #elif using time model
# time = int(input("enter the time of the day:"))
# if(time<12):
#     print("good morning baby")
# elif(time == 12):
#     print("it's noon")
# elif(time>12 and time<6):
#     print("goodafternoon")
# elif(time>6 and time<9):
#     print("good evening")
# elif(time>9 and time<12):
#     print("good night")
import time
t = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))
hour = int(input("enter the hour"))
print (hour)
if(hour <12):
    print("good morning baby")
elif(hour  == 12):
    print("it's noon")
elif hour >12 and(hour <6):
    print("goodafternoon")
elif hour >6 and(hour <9):
    print("good evening")
elif hour >9 and(hour <12):
    print("good night")
#(hour stamp = int(time.strftime('%H:%M:%S'))
# print(timestamp)
# timestamp = int (time.strftime('%H'))
# print(timestamp)
# timestamp = int(time.strftime('%M'))
# print(timestamp)
# timestamp = int(time.strftime('%S'))
# print(timestamp)
