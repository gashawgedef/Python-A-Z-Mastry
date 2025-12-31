"""Inventory management.

Demonstrates:
- Composition: Inventory contains Items.
- Aggregation: Items can exist independently.
- SOLID 'D': Depends on BaseItem abstraction.
- SOLID 'S': Only handles collection logic.
"""
from typing import List,Dict
from  weakref import WeakKeyDictionary
from .base import BaseItem

class Inventory:
    """Manages a collection of items (composition)."""
    def __init__(self,name:str):
        self.name = name
        self._items =List[BaseItem] =[]
        self._item_map =WeakKeyDictionary[str,BaseItem] = WeakKeyDictionary()
    def add_item(self,item:BaseItem)->None:
        """Adds an item (DependencyInjection)"""
        self._items.append(item)
        self._item_map[item.name] =item

    def remove_item(self,name:str)->None:
        item =self._item_map.get(name)
        if item:
            self._items.remove(item)
            del self._item_map[name]

    def get_total_value(self)->float:
        """Polymorphism: Calls get_price on each."""
        return sum(item.get_price() *item.quantity for item in self._items)

        