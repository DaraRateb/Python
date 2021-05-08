from bankaccount import BankAccount
class User:		
    def __init__(self,name,email_address):
        self.name = name
        self.email_address = email_address
        self.account = bankaccount()
    def make_withdrawal(self,amount):
        return self.account.withdraw(amount)
    def make_deposit(self,amount):
        return self.account.deposit(amount)
    def display_user_balance(self):
        return self.account.display_account_info(amount)
    def transfer_money(self, other_user, amount):
        if self.make_withdrawal(amount):
            other_user.deposit(amount)
            return True
        return False


