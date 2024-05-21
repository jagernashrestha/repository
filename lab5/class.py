class student:
    def __init__ (self,name,age,grade):
        self.naam = name
        self.age_no = age
        self.grade_sheet = grade 
    def show(self):
        print("name:",self.naam,"age:",self.age_no,"grade:",self.grade_sheet)
    
obj1 = student ('jagerna','19','99')
obj1.show()