""" Bank Account Class with deposit and withdraw methods and a display_info method to display the account holder self, account number and account balance."""
""" The init method takes in the account number, account balance and account holder self as parameters and assigns them to the instance variables of the class."""
""" The validate_account_number method takes in the account number as a parameter and checks if the account number is 9 digits long. If it is, it returns True. If it is not, it returns False."""
""" The validate_account_balance method takes in the account balance as a parameter and checks if the account balance is greater than or equal to 0. If it is, it returns True. If it is not, it returns False."""
""" The validate_account_holder_name method takes in the account holder self as a parameter and checks if the length of the account holder self is greater than 0. If it is, it returns True. If it is not, it returns False."""
""" The get_account_balance method returns the account balance."""
""" The get_account_number method returns the account number."""
""" The get_account_holder_name method returns the account holder self."""
""" The set_account_balance method takes in the account balance as a parameter and assigns it to the account balance instance variable."""
""" The set_account_number method takes in the account number as a parameter and assigns it to the account number instance variable."""
""" The set_account_holder_name method takes in the account holder self as a parameter and assigns it to the account holder self instance variable."""


class BankAccount:
    def validate_account_number(self, account_number):
        if len(str(account_number)) == 9:
            return True
        return False

    def validate_account_balance(self, account_balance):
        if account_balance >= 0:
            return True
        return False

    def validate_account_holder_name(self, account_holder_name):
        if len(account_holder_name) > 0:
            return True
        return False

    def __init__(self, account_number, account_balance, account_holder_name):
        self.account_number = self.validate_account_number(account_number)
        self.account_balance = self.validate_account_balance(account_balance)
        self.account_holder_name = self.validate_account_holder_name(
            account_holder_name)

    def get_account_balance(self):
        return self.account_balance

    def get_account_number(self):
        return self.account_number

    def get_account_holder_name(self):
        return self.account_holder_name

    def set_account_balance(self, account_balance):
        self.account_balance = account_balance

    def set_account_number(self, account_number):
        self.account_number = account_number

    def set_account_holder_name(self, account_holder_name):
        self.account_holder_name = account_holder_name

    '''The withdraw method takes in the amount to be withdrawn as a parameter and checks if the amount is greater than the account balance. If it is, it raises a ValueError. If it is not, it subtracts the amount from the account balance and returns the account balance.'''

    def withdraw(self, amount):
        if amount > self.account_balance:
            raise ValueError("You have insufficient funds in your account")
        self.account_balance -= amount
        return self.account_balance

    '''The deposit method takes in the amount to be deposited as a parameter and adds it to the account balance. It then returns the account balance.'''

    def deposit(self, amount):
        self.account_balance += amount
        return self.account_balance
    '''The display_info method returns a string containing the account holder self, account number and account balance.'''

    def display_info(self):
        return f"Account Holder Name: {self.account_holder_name}\nAccount Number: {self.account_number}\nAccount Balance: {self.account_balance}"


'''Create an instance of the BankAccount class and call the display_info method on the instance.'''
instance = BankAccount(123456789, 1000, "John Doe")
print(instance.display_info())
