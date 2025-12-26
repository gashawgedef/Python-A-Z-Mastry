from accounts.base import Account
class SavingsAccount(Account):
    interest_rate =0.03
    risk_level ="low"

    def get_ccount_type(self)->str:
        return "Savings"
    
    def apply_interest(self):
        interest =self.balance *self.interest_rate
        self.deposit(interest)
        self._log_transaction(f"Interest:+${interest:.2f}")
        