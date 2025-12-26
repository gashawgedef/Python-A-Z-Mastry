from accounts.base import Account
class LoanAcount(Account):
    interest_rate =0.05
    risk_level ="high"

    def __init__(self, customer, initial_balance:float = 0.0,loan_amount:float =0.0):
        super().__init__(customer, -loan_amount)
        self.loan_amount =loan_amount

    def get_ccount_type(self)->str:
        return "Loan"
    
    def pay_instalment(self,amount:float):
        if amount >0:
            self.deposit(amount)
            if self.balance >= 0:
                self._log_transaction("Loan is Fully Paid")

    def withdraw(self, amount:float)->bool:
        raise NotImplementedError("Can Not Withdraw From loan Account")
    
    