""" Bank Account Class with deposit and withdraw methods and a display_info method to display the account holder name, account number and account balance."""
""" The init method takes in the account number, account balance and account holder name as parameters and assigns them to the instance variables of the class."""
class BankAccount:
    def __init__(self, account_number,account_balance,account_holder_name):
        self.account_balance = account_balance
        self.account_number = account_number
        self.account_holder_name = account_holder_name
    
    '''The withdraw method takes in the amount to be withdrawn as a parameter and checks if the amount is greater than the account balance. If it is, it raises a ValueError. If it is not, it subtracts the amount from the account balance and returns the account balance.'''
    def withdraw(self, amount):
        if amount > self.account_balance:
            raise ValueError("Insufficient funds")
        self.account_balance -= amount
        return self.account_balance

    '''The deposit method takes in the amount to be deposited as a parameter and adds it to the account balance. It then returns the account balance.'''
    def deposit(self, amount):
        self.account_balance += amount
        return self.account_balance
    '''The display_info method returns a string containing the account holder name, account number and account balance.'''
    def display_info(self):
        return f"Account Holder Name: {self.account_holder_name}\nAccount Number: {self.account_number}\nAccount Balance: {self.account_balance}"

'''Create an instance of the BankAccount class and call the display_info method on the instance.'''
instance = BankAccount(123456789, 1000, "John Doe")
print(instance.display_info())