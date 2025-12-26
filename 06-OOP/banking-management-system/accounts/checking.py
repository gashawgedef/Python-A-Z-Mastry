from accounts.base import Account


class ChecingAccount(Account):
    over_draft_limmit =500.0
    risk_level ="medium"

    def get_ccount_type(self)->str:
        return "Checking"
    
    def withdraw(self, amount:float)->bool:
        if 0 <amount <=self.balance+self.over_draft_limmit:
            self.balance -= amount
            self._log_transaction(f"Withdrwal:-{amount:.2f}")
            return True
        return False
    
    