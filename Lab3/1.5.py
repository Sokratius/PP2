class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, transaction):
        self.balance += transaction
        print("Transaction done successful!!!")
        print("Now you have " + str(self.balance) + "$ on your account.\n")

    def withdraw(self, debit):
        if debit > self.balance:
            print("You have insufficient funds in your account.")
        else:
            self.balance -= debit
            print("You have just withdraw " + str(debit))
            print("Now you have " + str(self.balance) + "$ on your account.\n")


Robert_Lipnau = Account('Robert Lipnau', 999999999999)
Robert_Lipnau.withdraw(30000000)
Robert_Lipnau.deposit(2000000000)