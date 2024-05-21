for i in range(12):
    print("5 *", i+1, "=",5*(i+1))
    if (i==10):
        break
for i in range(12):
    if (i==10):
        print("skip iteration")
        continue
    print("5 *", i+1, "=",5*(i+1))

