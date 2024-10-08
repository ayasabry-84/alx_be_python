# bank_account.py
class BankAccount:
    def __init__(self, account_balance=0):  # Default balance is 0
        self.account_balance = account_balance

    def deposit(self, amount):
        """Add the specified amount to account_balance."""
        self.account_balance += amount  # Update the balance
        print(f"Deposited: ${amount:.1f}")  # Ensure to print with one decimal place

    def withdraw(self, amount):
        """Deduct the amount from account_balance if funds are sufficient."""
        if amount <= self.account_balance:
            self.account_balance -= amount  # Deduct the amount
            return True
        else:
            return False

    def display_balance(self):
        """Print the current balance in a user-friendly format."""
        print(f"Current Balance: ${self.account_balance:.2f}")  # Adjusted to two decimal places
