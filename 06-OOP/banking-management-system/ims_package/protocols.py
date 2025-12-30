from typing import Protocol
class Sellable(Protocol):
    def get_prices(self)->float:
        ...

    def apply_discount(self,percentage:float)->None:
        ...

class Stockable(Protocol):
    """Interface for Stock Management"""
    quantity:int
    def update_quantity(self,delta:int)->None:
        ...