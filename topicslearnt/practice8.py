# create account class
class Account:
    def __init__(self, balance, acc_no):
        self.balance = balance
        self.acc_no = acc_no

    def debit(self, balance):
        self.balance -= balance
        print("Rs. ", balance, " was deducted from your account.")

    def credit(self, balance):
        self.balance += balance
        print("Rs. ", balance, " was added from your account.")

    def print_balance(self):
        print("Your current balance is: ", self.balance)


A = Account(20000, 12345)
A.debit(1000)
A.credit(3000)
A.print_balance()
