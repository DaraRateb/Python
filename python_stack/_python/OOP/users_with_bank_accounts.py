from bankaccount import BankAccount
class User:		
    def __init__(self,name,email_address):
        self.name = name
        self.email_address = email_address
        self.account = bankaccount.BankAccount(int_rate=0.02, balance=0)
    def make_withdrawal(self,amount):
        return self.account.withdraw(amount)
    def make_deposit(self,amount):
        return self.account.deposit(amount)
    def display_user_balance(self):
        return self.account.display_account_info(amount)

laila = User('laila','laila@email')
laila.make_deposit(700)
laila.display_account_balance()


