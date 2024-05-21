class Atm:
    def __init__ (self):
        self.c_amt = c_amt
        self.name = input("enter name:")
        self.age = int(input("age:"))
        c_amt = int(input("enter the amount:"))
        self.address = input("enter address:")
        self.menu()
    def show_details(self):
        print("name:",self.name,"age:",self.age,end  = " ")
    def menu(self):
        print(f"1.show \n 2.deposit\n 3.withdraw \n ")
    def show(self):
        print("show current amount:", self.c_amt)
    def deposit(self): 
        d_amt = int(input("enter the amount to be deposit:"))
        self.c_amt += d_amt
        self.menu()
    def withdraw(self):
        w_amt = int(input('enter the amount to withdraw:'))
        if w_amt >= self.c_amt:
            print("withdrawn:",w_amt)
            print(f'current amount:',{self.c_amt-w_amt})
        else:
            print("insuffient amount")
        self.menu()
obj1 = Atm()
