num = input("ENTER YOUR MARK") 
if num.isdigit():
     mark = int(num)
#if isinstance (mark, int):   print(mark)

if mark>90:
     print("you scored distinction")  
elif mark<80:
     print("you scored first division")  
elif (mark<70):
     print("you scored second division")  
else:
     print("SORRY YOU FAILED")