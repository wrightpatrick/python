class User:
    account_balance = 0
    account_list = []

    def __init__(self, name):
        self.name = name
        self.account = BankAccount(int_rate = 0.02, balance = 0)
        User.account_list.append(self)
        

    def make_deposit(self, account_number, amount):
        self.account.balance += amount
        return self

    def make_withdrawl(self, account_number, amount):
        self.account.balance -= amount
        return self

    def display_user_balance(self):
        print(self.account.balance)
        return self

    def transfer_money(self, other_user, amount):
        self.account.balance -= amount
        other_user.balance += amount
        return self
        

class BankAccount:
    all_accounts = []

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
        
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds, how unfortunate. Now you must pay $5")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        self.balance = self.int_rate * self.balance + self.balance
        return self

charlie = User('Charlie')
barbie = User('Barbie')
reginald = User('Reginald')

print(BankAccount.all_accounts)