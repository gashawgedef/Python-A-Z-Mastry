
from abc import ABC,abstractmethod
from typing import Any
from .constants import ItemCategory

class BaseItem(ABC):
    """Abstract base class for all items(Abstractions)"""
    def __init__(self,name:str,price:float,quantity:int,category:ItemCategory):
        self._name =name
        self.__price =price
        self.quantity = quantity
        self.category =category
    @property
    def name(self)->str:
        """Getter for name or encapsulation"""
        return self._name
    
    @name.setter
    def name(self,value:str)->None:
        if not value:
            raise ValueError("Name can not be empty")
        self._name =value

    @abstractmethod
    def get_price(self)->float:
        pass

    def __str__(self)->str:
        return f"{self.name} ({self.category.name}):{self.get_price():.2f} *{self.quantity}"
    