class Bank:
    acc_no:int
    acc_holder_name:str
    acc_type:str
    balance:int

    def __init__(self, acc_no, acc_holder_name, acc_type, balance):
        self.acc_no = acc_no
        self.acc_holder_name = acc_holder_name
        self.acc_type = acc_type
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}")

    def withdraw(self, amount):
        if amount <= self.balance :
            self.balance -= amount
            print(f"{amount} withdrawed from your account")
        else:
            print("Insufficient balance")

    def get_balance(self):
        print(f"Account holder name : {self.acc_holder_name}")
        print(f"Balance : {self.balance}")


account_1 = Bank(764635337875, "Ashik Vincent", "Savings", 1200)


# account_1.create_account(764635337875, "Ashik Vincent", "Savings", 1200)

account_1.get_balance()

account_1.deposit(200)

account_1.get_balance()

account_1.withdraw(100)

account_1.get_balance()

account_1.withdraw(1300)

account_1.get_balance()