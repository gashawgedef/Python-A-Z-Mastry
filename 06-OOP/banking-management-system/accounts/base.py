
from abc import ABC,abstractmethod
import datetime
class AccountMeta(type):
    def __new__(cls,name,bases,dict):
        if 'risk_level' not in dict:
            raise TypeError(f"{name} must define 'risk_level'")
        return super().__new__(cls,name,bases,dict)
    
class Account(ABC,metaclass =AccountMeta):
    _account_counter = 1000
    risk_level = "base"

    def __init__(self,customer, initial_balance:float=0.0):
        self.account_number = f"ACC{Account._account_counter}"
        Account._account_counter +=1
        self.customer =customer
        self._balance =initial_balance
        self.transaction_history =[]
        customer.add_account(self)

    @abstractmethod
    def get_ccount_type(self)->str:
        pass

    @property
    def balance(self)->str:
        return self._balance
    
    @balance.setter
    def balance(self,value:float):
        if value>=0:
            self._balance =value
        else:
            raise ValueError("Balance Can not be negative")
        
    def deposit(self,amount:float)->bool:
        if amount >0:
            self._balance += amount
            self._log_transaction(f"Deposit:+${amount:.2f}")
            return True
        return False
    
    def withdraw(self,amount:float)->bool:
        if 0< amount <= self._balance:
            self._balance -= amount
            self._log_transaction(f"Withdrwal: -${amount:.2f}")
            return True
        return False
    
    def _log_transaction(self,msg:str):
        timestamp  = datetime.datetime.now.isoformat()
        self.transaction_history.append(f"[{timestamp}] {msg}")


    def __str__(self)->str:
        return f"{self.get_ccount_type()} {self.account_number}:{self.balance:.2f}"
    
    def __add__(self,other):
        if isinstance(other,Account) and self.customer == other.customer:
            new_balance =self.balance +other.balance
            new_account =type(self)(self.customer,new_balance)
            new_account.transaction_history =self.transaction_history + other.transaction_history
            return new_account
        raise ValueError("Can Not Merge The Two Accounts")
    
    def __len__(self)->int:
        return len(self.transaction_history)



    