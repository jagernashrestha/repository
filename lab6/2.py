# 2,Create a base class Person with attributes name and age. Derive two classes, Student and Teacher. 
# 	Student should have an additional attribute grade, 
# 	and Teacher should have an additional attribute subject. and show details of student and teacher.


class person:
    def __init__(self,name,age):
        self.age = age
        self.name = name


class student(person):
    def __init__(self,name,age,grade):
        self.grade  = grade
        print("grade : ",self.grade)
        super().__init__(name, age)
    def show(self):
        print(self.name, self.age,self.grade)

class teacher(person):
    def __init__(self,name,age,department):
        self.department = department
        super().__init__(name, age)
    def show(self):
        print(self.name, self.age,self.department)
obj1 = student("aravika",23,90)
obj2 = teacher("jagerna",19,'computer')
obj1.show()
obj2.show()