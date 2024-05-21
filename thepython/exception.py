def add(a,b):
    try:
        sum = int(a)+int(b)
        print(sum)
    except Exception as e:
            print(e.__class__)
    finally:
        print("this is the end")