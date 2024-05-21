print("decotator")
def greet(fx):
    def mfx(*args,**kwargs):
        print("good morning")
        fx(*args,**kwargs)
        print("thanks for using functions")
        return mfx
@greet
def hello():
    print("hello jagerna")
@greet
def add(a,b):
    print(a+b)