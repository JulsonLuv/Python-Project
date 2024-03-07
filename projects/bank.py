class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    @property
    def account_info(self):
        return f"Account Owner: {self.owner}, Balance: ${self.balance}"

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds.")

    def transfer(self, recipient, amount):
        if amount <= self.balance:
            self.balance -= amount
            recipient.balance += amount
            print(f"Transferred ${amount} to {recipient.owner}. Your balance: ${self.balance}")
        else:
            print("Insufficient funds.")