x = int(input("enter the number:"))
match x:
    case 0:
        print("case is zero")
    case 1:
        print("case is 1")
    case _:
        print(x)