class User:
    account_balance = 0

    def __init__(self, name):
        self.name = name
        

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawl(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(self.account_balance)
        return self

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self
        



chad = User('chad')
monica = User('monica')
peter = User('peter')

chad.make_deposit(300).make_deposit(200).make_deposit(100).make_withdrawl(200).display_user_balance()
# chad.make_deposit(200)
# chad.make_deposit(100)


# chad.display_user_balance()

# chad.make_withdrawl(200)

# chad.display_user_balance()

monica.make_deposit(1000).make_deposit(500).display_user_balance().make_withdrawl(150).make_withdrawl(350).display_user_balance()
# monica.make_deposit(500)

# monica.display_user_balance()

# monica.make_withdrawl(150)
# monica.make_withdrawl(350)

# monica.display_user_balance()

peter.make_deposit(1000).make_deposit(250).display_user_balance()
# peter.make_deposit(250)

# peter.display_user_balance()

chad.transfer_money(peter, 400).display_user_balance()

# chad.display_user_balance()
peter.display_user_balance()
