
from enum import Enum,auto
class ItemCategory(Enum):
    """Category for Items"""
    ELECTRONICS =auto()
    DIARY  = auto()
    CLOTHING = auto()
    BOOKS = auto()
  
class Orderstatus (Enum):
    """Order processing States"""
    PENDING = auto()
    PROCESSED =auto()
    CANCELED = auto()

