

from accounts.base import Account

class Transaction:

    def __init__(self,from_account:Account,to_account:Account,amount:float):
        self.from_account =from_account
        self.to_account = to_account
        self.amount =amount
    def execute(self)->bool:
        if self.from_account.withdraw(self.amount):
            self.to_account.deposit(self.amount)
            self.from_account._log_transaction(f"Transfer out to {self.to_account.account_number}:-${self.amount:.2f}")
            self.to_account._log_transaction(f"Transfer in from {self.from_account.account_number}:+${self.amount:.2f}")
            return True
        return False
    
    @staticmethod
    def validate_transfer(from_account:Account,to_account:Account,amount:float)->float:
        return amount >0 and from_account != to_account
    