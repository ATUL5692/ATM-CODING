class Atm:
    def __init__(self):
        self.pin = 1010
        self.balance = 1000
        self.menu()
    def menu(self):
        user_input = input("""
                                      Hello, How you want to proceed?
                                      1. Enter 1 to create pin.
                                      2. Enter 2 to deposit money.
                                      3. Enter 3 to withdraw money.
                                      4. Enter 4 to check balance.
                                      5.Enter 5 to exit.
""")
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
    def create_pin(self):
        self.pin = int(input("create your pin:"))
        print("PIN created sucessfully")
    def deposit(self):
        a = int(input("Enter your PIN:"))
        if self.pin ==a:
            amount = int(input("Enter your amount you want to deposit:"))
            self.balance = self.balance + amount
            print("Total Amount  after deposit is:", self.balance)
        else:
            print("Invalid PIN")
            
