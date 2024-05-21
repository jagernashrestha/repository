import sys
def test1(value):
    print(f'my name is {value}')

#method
class jagerna:
    def test(self, value):
        print(f'my name is {value}')
obj = jagerna()
obj.test("arav")
# test1("arav")
print(sys.getsizeof(test1))
