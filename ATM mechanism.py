"""For this challenge, create a bank account class that has two attributes:

owner
balance
and two methods:

deposit
withdraw"""
class Account:
    def __init__(self, Accountant_name, bank_balance=500):
        self.Accountant_name = Accountant_name
        self.bank_balance = bank_balance
    def owner(self):
        return self.Accountant_name
    def balance(self):
        return self.bank_balance
    def deposit(self, amount):
        self.bank_balance += amount
        return self.bank_balance
    def withdraw(self,ammount):
        if ammount <= self.bank_balance:
            self.bank_balance -= ammount
            return self.bank_balance
        else:
            print("Insufficient Balance.Please Check Your Balance")
 
details = input("Enter owner and initial balance (comma-separated): ").split(",")
Accountant_name = details[0]
bank_balance= float(details[1])
acct1 = Account(Accountant_name,bank_balance)
print("ACCOUNT OWNER:",acct1.owner())
print("ACCOUNT BALANCE:",acct1.balance())
operation = int(input("Enter '1.deposit' or '2.withdraw' to perform the operation: "))
if operation==1 :
    ammount_deposite = float(input("Please Enter The Amount To Be Deposited:"))
    print("Balance After Deposite:",acct1.deposit(ammount_deposite))
elif operation == 2: 
    ammount_withdraw = float(input("Please Enter The Amount To Be Withdrawn:"))
    print("Balance After Withdraw:",acct1.withdraw(ammount_withdraw))
else:
    print("Invalid operation. Please choose either 'deposit' or 'withdraw'.")

print("THANKYOU PLEASE VISIT AGAIN!")
