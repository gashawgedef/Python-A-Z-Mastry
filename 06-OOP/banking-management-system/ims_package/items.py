"""Item classes extending base.

Demonstrates:
- Inheritance and polymorphism.
- Composition: Items can compose with other objects if needed.
- SOLID 'S': Each subclass handles specific concerns (e.g., perishability).
- SOLID 'L': PerishableItem can substitute BaseItem.
"""

from datetime import datetime ,timedelta
from .base import BaseItem
from .protocols import Sellable,Stockable
from .constants import ItemCategory

class StandardItem(BaseItem,Sellable,Stockable):
    """Standard non-perishable item.

    Implements protocols for segregation.
    """
    def __init__(self, name:str, price:float, quantity:int, category:ItemCategory):
        super().__init__(name, price, quantity, category)
        self.discount = 0.0

    def get_price(self)->float:
        return self.get_price*(1-self.discount)
    
    def apply_discount(self, percentage:float)->None:
       """From Sellable Protocol"""
       self.discount =min(1.0,max(0.0,percentage/100))

    def update_quantity(self, delta:int)->None:
       """From Stockable Protocol"""
       self.quantity +=delta
       if self.quantity <0:
           raise ValueError("Quantity can not be negative")
       
class PerishableItem(StandardItem):
   """Extends StandardItem for perishables (inheritance).

    Demonstrates polymorphism by overriding.
    SOLID 'O': Extended without modifying base.
    """
   def __init__(self, name:str, price:float, quantity:int, category:ItemCategory,expiry_days:int):
       super().__init__(name, price, quantity, category)
       self.expiry_date = datetime.now()+timedelta(days=expiry_days)
       
   def  get_price(self)->float:
        """Overrides: Reduces price if near expiry (polymorphism)."""
        days_left = (self.expiry_date - datetime.now()).days
        reduction  = 0.5 if days_left < 3 else 0.0
        return super().get_price()*(1-reduction)
   
   def is_expired(self)->bool:
       return self.expiry_date <datetime.now()