"""Advanced OOP features.

Demonstrates:
- Metaclass: For auto-registration.
- Descriptor: For validated attributes.
- Total Ordering: For comparable items.
- Monkey-patching: Demo extension.
"""

from typing import Any, Dict, Type
from functools import total_ordering

class AutoRegisterMeta(type):
    """Metaclass: Registers subclasses automatically."""
    registry: Dict[str, Type] = {}

    def __new__(cls, name: str, bases: tuple, dct: Dict[str, Any]):
        new_cls = super().__new__(cls, name, bases, dct)
        if name != 'BaseItem':  # Avoid base
            cls.registry[name] = new_cls
        return new_cls

# Apply metaclass (advanced inheritance)
from .base import BaseItem
BaseItem = AutoRegisterMeta('BaseItem', BaseItem.__bases__, dict(BaseItem.__dict__))

class PriceDescriptor:
    """Descriptor for validated price."""

    def __get__(self, instance: Any, owner: Type) -> float:
        return instance._price

    def __set__(self, instance: Any, value: float) -> None:
        if value < 0:
            raise ValueError("Price cannot be negative")
        instance._price = value

# Total ordering example
@total_ordering
class ComparableItem:
    """Demo class with rich comparisons."""

    def __init__(self, value: int):
        self.value = value

    def __eq__(self, other: Any) -> bool:
        return self.value == other.value

    def __lt__(self, other: Any) -> bool:
        return self.value < other.value

# Monkey-patching demo (extend existing class)
from .items import StandardItem

def extra_method(self):
    return f"Extra: {self.name.upper()}"

StandardItem.extra = extra_method