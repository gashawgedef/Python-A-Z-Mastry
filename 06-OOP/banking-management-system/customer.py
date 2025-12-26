from accounts.base import Account

class Customer:
    def __init__(self, name:str,customer_id:str,ssn:str):
        self.name =name
        self.customer_id =customer_id
        self.__ssn =ssn
        self.accounts =list[Account]=[]
        self.loans =[]

    @property
    def ssn(self)->str:
        return "XXX-XX"+self.__ssn[-4:]
    
    @ssn.setter
    def ssn(self,value:str):
        if len (value)==9 and value.isdigit():
            self.__ssn =value
        else:
            raise  ValueError("Invalid SSN")
        
    def add_account(self,account:Account):
        self.accounts.append(account)

    def add_loan(self,loan):
        self.loans.append(loan)

    def get_total_balance(self)->float:
        return sum(acc.balance for acc in self.accounts)
     
    def __str__(self)->str:
        return f"Customer:{self.name} (ID:{self.customer_id})"
    
    def __repr__(self)->str:
        return f"Customer(name='{self.name}',customer_id ='{self.customer_id}')"
    
    def __eq__(self, value)->bool:
        if isinstance(value,Customer):
            return self.customer_id ==value.customer_id
        else:
            return False

    @classmethod
    def from_dict(cls,data:dict):
        return cls(data['name'],data['customer_id'],data['ssn'])
            
    

    