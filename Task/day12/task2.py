'''
Bank Account System
Create a class BankAccount with attributes like account_number, owner_name, and balance.
Include methods for:
Depositing money.
Withdrawing money (ensure sufficient balance).
Checking the account balance.
'''

class BankSystem:
    
    def __init__(self,account_number,owner_name,balance):
        self.account_number=account_number
        self.owner_name=owner_name
        self.balance=balance

    def deposit(self,deposit_amount):
        if deposit_amount<0:
            print("You cannot deposit balance in negative")
        else:
            self.balance += deposit_amount
            print(f"Your deposited amount is {deposit_amount} and your new balance is {self.balance}")

    def withdraw(self,withdraw_amount):
        if withdraw_amount<0:
            print("You cannot withdraw balance in negative")
        elif withdraw_amount>self.balance:
            print("You don't have sufficient balance")
        else:
            self.balance -= withdraw_amount
            print(f"Your withdrawn amount is {withdraw_amount} and your new balance is {self.balance}")

    def show_balance(self):
        print(f"Your account balance is {self.balance}")


acc1=BankSystem(1,"Ashiwn",500)
acc1.deposit(5000)
acc1.withdraw(2000)
acc1.show_balance()