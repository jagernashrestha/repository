import pandas as pd

list1 = [['jagerna',19,'sitapaila'],['sharbes',12,'sitapaila'],['aryav',23,'samakushi']]
a = pd.DataFrame(list1,columns = ['name','age','address'])
print(a)