#area of circle and circumference
import math

radius1 = int(input("enter the radius"))
area = math.pi * radius1 **2
circum = 2*math.pi*radius1
print(f'area ={ round(area ,2)}, area,circum = {circum, round(circum,2)})')
