# Static methods.

class BankAccount:
    MIN_BALANCE = 100 # convention: capitlize constant values. This is shared across all instances.
    
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self._balance = balance
    
    def deposit(self, amount):
        if self._is_valid_amount(amount):
            self._balance += amount
            self.__log_transaction("deposit", amount)
            print(f'{self.owner} new balance: ${self._balance}')
        else:
            print("Deposit amount must be postiive.")
    
    # Static methods are useful for utility functions or format data.
    
    @staticmethod
    def is_valid_interest_rate(rate):
        return 0 <= rate <= 5
    
    # Protected method
    def _is_valid_amount(self, amount):
        return amount > 0
    
    # Private method
    def __log_transaction(self, transaction_type, amount):
        print(f"Logginf {transaction_type} of ${amount}. New balance: $ {self._balance}")
    
account = BankAccount("Alice", 500)
account.deposit(200)

print(BankAccount.is_valid_interest_rate(3))
print(BankAccount.is_valid_interest_rate(10))