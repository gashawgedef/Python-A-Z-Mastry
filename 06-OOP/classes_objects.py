# """
# File: classes_objects.py
# Author: Gashaw Gedef
# Purpose: To be filled
# """
class Doors:
    height:str
    color:str
    is_locked:bool

    def __init__(self,height:str,color:str,is_locked:bool):
        self.height=height
        self.color =color
        self.is_locked=is_locked

    def make_paint(self):
        return f"{self.color} is the classes color"

dor1=  Doors(1.75,"red",False)
color =dor1.make_paint()
print(color)


"""Bundling data and methods, with access control using _ (protected) or __ (private, name-mangled)."""

class BankAccount:
    district="Gondar District"
    def __init__(self,balance):
        self.__balance =balance

    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount

    def get_balance(self):
        return self.__balance
    
account =BankAccount(1000)
account1=BankAccount(500)
account.deposit(500)
print(account.get_balance())
print(account.district)
print(account1.get_balance())
print(account1.district)

