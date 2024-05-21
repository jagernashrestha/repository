class Square:
    def __init__(self,length):
        self.length = length
    def area(self,length):
        return length*length
    def perimeter(self,l):
        self.length = l
        return 4*self.length
obj1 = Square(10)
area = obj1.area(10)
perimeter = obj1.perimeter(10)
print(area,perimeter)