'''class animal:
    def eat(self):
        print('eat')
class dog (animal):
    def eat(self):
        super().eat()#super() help to access parent's attributes it is a function 
        print("animal")
a = dog()#object formation
a.eat()#method call'''

'''class person:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(self.name)

class hari  (person):
    def show1(self):
        print('child class')

h = hari('ram')
h.show()'''

'''class collage:
    def __init__(self, name, location, phone):#attributes
        self.name=name
        self.location=location
        self.phone=phone
    def show(self):
        print(self.name)

class computer(collage):
    def __init__(self,sem,total_subject,name,location,phone):#attribute
        print('child class')
        self.sem = sem
        self.total_subject = total_subject
        super().__init__(name,location,phone)
    def show(self):
        print(self.name)
        print(self.phone)
        print(self.total_subject)
        print(self.sem)
        print(self.location)
object = computer(7,4,'acme','sitapaila','015140009')
object.show()'''

'''class ColdDrinks:
    def __init__(self, name,price):
        self.name = name
        self.price = price
    def display(self):
        print("Name : ",self.name,"\nPrice : ",self.price)
class Customer(ColdDrinks):
    def __init__(self,quantity,name,price):#attribute
        print('child class')
        self.quantity = quantity
        super().__init__(name,location,phone)
    def show(self):
        print(self.name)
        print(self.phone)
        print(self.total_subject)
        print(self.sem)
        print(self.location)
object = computer(7,4,'acme','sitapaila','015140009')
object.show()
'''
# class student:
#     def __init__(self,name,):
#         self.name=name
        
# s = student('ram')
# print(hasattr(s,'name'))
# print(getattr(s,'name1', 'if'))
# setattr(s,'age',23)
# delattr(s,'age')
# print(getattr(s,'age'))
