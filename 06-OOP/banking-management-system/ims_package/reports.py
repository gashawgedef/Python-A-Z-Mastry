"""Reporting utilities.

Demonstrates:
- Decorator: For logging.
- Context Manager: For file handling.
- SOLID 'S': Only reporting concerns.
"""

from typing import Callable
from functools import wraps
import os

def log_report(func:Callable)->Callable:
    """Decorator to log report generation"""
    @wraps(func)
    def wrapper (*args,**kwargs):
        print(f"Generating report:{func.__name__}")
        return func(*args,**kwargs)
    return wrapper
@log_report
def generate_report(inventory:'Inventory')->str:
    """Generates inventory report (polymorphism in str(item))."""
    report = f"Inventory: {inventory.name}\n"
    for item in inventory._items:
        report+=f"-{str(item)}\n"
    report += f"Total Value: ${inventory.get_total_value():.2f}"
    return report

class ReportContext:
    """Context manager for report files."""

    def __init__(self, filename: str):
        self.filename = filename
        self.logs: list[str] = []

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open(self.filename, 'w') as f:
            f.write('\n'.join(self.logs))
        if exc_type:
            os.remove(self.filename)  # Cleanup on error

    def log(self, message: str) -> None:
        self.logs.append(message)