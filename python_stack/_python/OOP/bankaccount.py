class BankAccount:
    def __init__(self, int_rate, balance): 
        self.int_rate=0
        self.balance=balance
    def deposit(self, amount):
        self.balance=self.balance+amount
    def withdraw(self, amount):
        self.balance=self.balance-amount
    def display_account_info(self):
        print(f"Interest Rate: {self.int_rate} Balance: {self.balance}")
    def yield_interest(self,int_rate):
        self.balance=self.balance+(self.balance*self.int_rate)

Dara=BankAccount(0.05,5000)
Amira=BankAccount(0.03,3000)
Dara.display_account_info()

Dara.deposit(3000)
Dara.deposit(1000)
Dara.deposit(5000)
Dara.withdraw(4000)
Dara.yield_interest(0.5)
Dara.display_account_info()




