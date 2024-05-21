# single (_)is for protected variables (__)double is for private and not used for public
# private so name can't be changedd
# here name is private so it can't be accesed and changed error occcurs
# using name manglingx in private variables
class person:
    def __init__(self, name, age):
        self.__namdde = name
p1 = person('jagerna',19)
print(p1._person__namdde)
### yo haru bataa mildainaaa changee garnaaaaaaaaaaaaaaaa
# class student:
#     def __init__(self,name):
#         self.__NaamBhanaTaSathi = name
# s1 = student('Jagerna')
# print(s1.___NaamBhanaTaSathi)

# class person:
#     def __init__(self, name, age):
#         self.__namdde = name
# p1 = person('jagerna',19)
# print(p1.__namdde)