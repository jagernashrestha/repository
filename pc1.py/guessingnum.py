import numpy as np
count = 0
arr1 = np.random.randint(0,10)
print(arr1)
while True:
    print("pprint the random number:")
    n1 = int(input("enter the number:"))
    if n1 == arr1:
        count +=1
        print("you win")
    else:
        print("you lose")
    
    
