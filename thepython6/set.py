# set use garera hamle private variables ko value change garna sakxa
class person:
    # syntax :: def __init__(self,parameter):
    def __init__(self, name, age):
        self.__namdde = name
        self. __year = age
    # def set _className_variableName(self, parameter)
    def set_person_year(self, age):
        self. __year = age
p1 = person('jagerna','19')
p1.set_person_year(30)
print(p1._person__year)