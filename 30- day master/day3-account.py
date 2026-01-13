
from decimal import Decimal

class Account:
    def __init__(self,owner:str,balance:float = 0.0):
        self.owner =owner
        self._balance =Decimal(str(balance))

    def __repr__(self):
        return f"Account(owner ={self.owner!r},balance ={self._balance})"
    
    def __str__(self):
        return f"{self.owner}'s account:${self._balance:.2f}"
    
    def __eq__(self, value):
        if not isinstance(value,Account):
            return NotImplemented
        return self.owner ==value.owner and self._balance ==value._balance
    def __hash__(self):
        return hash((self.owner,self._balance))
    
    
    

account =Account("Gashaw Gedef",2000)

print(account)