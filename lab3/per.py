from fact import fact
n = int(input("Enter the number: "))
r = int(input("Enter the r: "))
f1 = fact(n)
f2 = fact(n-r)
a = f1/f2
c=a/fact(r)
print(a)

print(c)