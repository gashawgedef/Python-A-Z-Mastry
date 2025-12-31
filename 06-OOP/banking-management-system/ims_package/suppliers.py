
"""Suppliers and orders.

Demonstrates:
- Aggregation: Order aggregates Items and Supplier.
- SOLID 'S': Supplier handles supply, Order handles processing.
"""
from typing import Dict
from .base import BaseItem
from .inventory import Inventory
from .constants import Orderstatus

class Supplier:
    """Supplier Entity"""
    def __init__(self,name:str):
        self.name =name
    
class Order:
    """Order from Supplier (Aggrefgation of items)"""
    def __init__(self,supplier:Supplier,items:Dict[BaseItem,int]):
        self.supplier = supplier
        self.items = items
        self.Status =Orderstatus.PENDING
    def process(self,inventory:Inventory)->None:
        """Update Inventory (Interaction)"""
        for item ,qty in self.items.items():
            item.update_quantity(qty)
        self.Status =Orderstatus.PROCESSED
