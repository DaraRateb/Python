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

Dara=BankAccount(0.05,5000)
Amira=BankAccount(0.03,3000)
#Dara.display_account_info()

Dara.deposit(3000).deposit(1000).deposit(5000).withdraw(4000).yield_interest(0.8).display_account_info()
Amira.deposit(4000).deposit(6000).withdraw(100).withdraw(50).withdraw(50).withdraw(300000).display_account_info()


