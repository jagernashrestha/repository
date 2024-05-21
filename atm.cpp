class Atm:
    def __init__(self, balance, name, age, address):
        self.balance = balance
        self.name = name
        self.age = age
        self.address = address
        self.menu()

    def menu(self):
        user_input = input("""
                1.Check Balance
                2.Deposit Balance
                3.Withdraw Balance
                4. User Details
                """)
        if user_input =="1":
            self.check_Balance()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.user_details()
        else:
            exit()
        
    def check_Balance(self):
        print(f"Your current balance is {self.balance}")
        self.menu()
    def deposit(self):
        d_amount = int(input("Enter amounyt to be deposit:"))
        self.balance =self.balance+d_amount
        self.menu()
    def withdraw(self):
        w_amount = int(input("Enter amounyt to be withdraw:"))
        if self.balance>=w_amount:
            self.balance =self.balance-w_amount
            print(f"Balance has been withdraw success.")
        else:
            print("insufficient balanec.")

        self.menu()
    def user_details(self):
        print(f"")
        self.menu()
        
atm = Atm(1000, 'ram', 20, 'ktm')