

from accounts.savings import SavingsAccount
from audit import AuditableMixin

class PremiumAccount(SavingsAccount,AuditableMixin):
    bonus_rate =0.01
    risk_level="low-premium"

    def __init__(self, customer, initial_balance:float = 0.0):
        super().__init__(customer, initial_balance)
        self.audit_log = []

    def get_ccount_type(self)->str:
        return "Premium Savings"
    
    def apply_interest(self):
        super().apply_interest()
        bonus =self.balance * self.bonus_rate
        self.deposit(bonus)
        self._log_transaction(f"Premium Bonus:+${bonus:.2f}")
        self.log_audit("Interest And Bonus are applied")
        
    