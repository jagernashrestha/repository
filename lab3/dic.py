#to generate  dicionary
def dictionary1(a):
    d1 = { }
    for i in range(1,a):
        key = i
        value = i**2
        d1[key] = value
    return d1
num = int(input("Enter the number: "))

if num>0:
    print(dictionary1(num))
else:
    print("Enter positive nummber")

