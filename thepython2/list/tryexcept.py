try:
    l1 = [10,30,20]
    l2 = sorted (l1)
    print(l1[12])

except ValueError as n:
    print("arav")
except TypeError as e:
    print("astro")
except NameError as e:
    print(" Aryav")
except IndexError as e:
    print("moon")
except ValueError as e:
    print("tutu")
except ValueError as e:
    print("nanan")
except Exception as v:
    print("ERRORR OCCURED")
finally:
    print(l1)