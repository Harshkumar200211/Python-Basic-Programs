"""78. Encapsulation with a Bank Account

Python practice program 78 of 100.
"""

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def show_balance(self):
        print(self.owner, "balance:", self.__balance)

account = BankAccount("Aman", 1000)
account.deposit(500)
account.show_balance()
