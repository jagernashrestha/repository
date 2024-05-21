name = "jagerna"
print (name [2])
print (name [5])
#lets use a for loop
for character in name:
    print(character )

chaaaa = "jagerna , jagga, bukkie"
print (chaaaa [0:6])
print (chaaaa [0:8])
print (chaaaa [:])

chaaaa = "bukkie"
print (chaaaa [0:-3])
len1 = len(chaaaa)
print("heheheh is a ", len1, "lettrrrrr worddddddd")
print(chaaaa[-1:len(chaaaa) -3])
# including -3 but not -1
print (chaaaa [-3:-1])
nm = "jager"
print(nm[-4:-2])
a = "aryav!!!!!!!!!!!!!"
# string is immutable
print (len (a))
print (a.upper())
print (a.lower())
print (a.rstrip())
print(a.replace("aryav","Jagerna"))
print(a.split("2"))
blogHeading = "introduction to jS"
print(blogHeading.capitalize())
str1 = "Welcome to the Console!!!"
print(len (str1.center(50)))
a = "aryav!!!!!!!!!!!!!"
print(len(str1))
print(a.count("Aryav"))
str1 = "Welcome to the Console!!!"
print(str1.endswith("!!!"))