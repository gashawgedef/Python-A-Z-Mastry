from abc import ABC, abstractmethod
from dataclasses import dataclass
from .enums import ItemStatus

class LibraryItem(ABC):
    total_items = 0  # Class attribute
    
    def __init__(self, title):
        self._title = title
        self.__item_id = id(self)
        self.status = ItemStatus.AVAILABLE
        LibraryItem.total_items += 1
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if len(value.strip()) > 0:
            self._title = value.strip()
    
    @abstractmethod
    def display_info(self):
        pass
    
    def __str__(self):
        return f"{self.title} (ID: {self.__item_id}) - {self.status.value}"

class Book(LibraryItem):
    __slots__ = ['author', '_title', '__item_id', 'status']  # Memory optimization
    
    def __init__(self, title, author):
        super().__init__(title)
        self.author = author
    
    def display_info(self):
        return f"Book: {self.title} by {self.author}"

class DVD(LibraryItem):
    def __init__(self, title, duration):
        super().__init__(title)
        self.duration = duration
    
    def display_info(self):
        return f"DVD: {self.title} ({self.duration} mins)"