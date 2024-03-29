
class BankAccount:
    def __init__(self, int_rate=0.01, balance=0): 
        self.int_rate=int_rate
        self.balance=balance
    def deposit(self, amount):
        self.balance=self.balance+amount
        return self
    def withdraw(self, amount):
        if amount<=self.balance:
            self.balance=self.balance-amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance=self.balance-5
        return self
    def display_account_info(self):
        print(f"Interest Rate: {self.int_rate} Balance: {self.balance}")
        return self
    def yield_interest(self,int_rate):
        self.balance=self.balance+(self.balance*self.int_rate)
        return self
class User:		
    def __init__(self,name,email_address):
        self.name = name
        self.email_address = email_address
        self.account = BankAccount()
    def make_withdrawal(self,amount):
        return self.account.withdraw(amount)
    def make_deposit(self,amount):
        return self.account.deposit(amount)
    def display_user_balance(self):
        return self.account.display_account_info()

laila = User('laila','laila@email')
laila.make_deposit(700)
laila.display_user_balance()


