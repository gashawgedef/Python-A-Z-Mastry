"""
File: inheritance.py
Author: Gashaw Gedef
Purpose: To be filled
"""
from abc import ABC,abstractmethod

class Payment(ABC):
    @abstractmethod
    def process(self,amount):
        pass

class CreditCard(Payment):
    def process(self,amount):
        return f'Processed ${amount} via Credit Card'


