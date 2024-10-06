class BankAccount:

# class variables
    interest_rate = 0.05

# constructor  
    def __init__(self, account_holder, balance=0): 

        # instance variables 
        self.account_name = account_holder
        self.balance = balance

# method to deposit money
    def deposit(self,amount):
        self.balance += amount
        
        
# method to withdraw money
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else: self.balance -= amount
        

# method to apply interest rate
    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        

# Method to display_account_info when requested
    def display_account_info(self):
        print(f"Account Name: {self.account_name}")
        print(f"Current Balance: shs.{self.balance}")
        
        

# creating instances of the class BankAccount
account1 = BankAccount("Charity Aber")    
account2 = BankAccount("Andrew Wasswa")
account3 = BankAccount("Tish Peters") 

# Perform deposits and withdrawals
account1.deposit(1000000)
account1.withdraw(50000)

account2.deposit(500000)
account2.withdraw(90000)

account3.deposit(5000000)
account3.withdraw(400000)

# applying the interest rates on the accounts balances
account1.apply_interest()
account2.apply_interest()
account3.apply_interest()

# Displaying account information eg.accountholder and current balance after applying interest.
# ()the parathesis calls the method 
account1.display_account_info()
account2.display_account_info()
account3.display_account_info()

  




