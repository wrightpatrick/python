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

    

account1 = BankAccount(.03, 40000)
account2 = BankAccount(.01, 100000)

print(account1.balance)

account1.yield_interest()

print(account1.balance)

account1.deposit(4500).deposit(5000).deposit(16).withdraw(20000).display_account_info()

account2.deposit(10000).deposit(10000).withdraw(100).withdraw(195).yield_interest().display_account_info()

print(account1)

print(BankAccount.all_accounts)
