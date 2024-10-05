class Account:
    def __init__(self, name, start_balance):
        self.name = name
        self.balance = start_balance
        self.history = ''

    def add_money(self, money):
        self.balance += money
        self.history += f"{money} added\n"

    def withdraw_money(self, money):
        self.balance -= money
        self.history += f"{money} withdrawn\n"


