# Project: Advanced OOP Demonstration - Inventory Management System (IMS)

This project is a comprehensive Python implementation showcasing Object-Oriented Programming (OOP) concepts from foundational to advanced levels. It models a simple **Inventory Management System (IMS)** for a retail store, handling items, categories, suppliers, orders, and reporting.

## Key Features and Goals
- **Depth**: Starts with basic OOP (classes, objects) and progresses to advanced topics (metaclasses, descriptors, context managers, decorators, etc.).
- **Documentation**: Extensive docstrings, inline comments, and module-level explanations.
- **File Structure**: Organized as a Python package (`ims_package`) for modularity and reusability.
- **SOLID Principles**:
  - **S**ingle Responsibility: Each class handles one concern (e.g., `Item` manages item data, `Inventory` manages collections).
  - **O**pen-Closed: Classes are open for extension (e.g., via inheritance for new item types) but closed for modification (e.g., core methods aren't altered directly).
  - **L**iskov Substitution: Subclasses (e.g., `PerishableItem`) can replace base classes without breaking behavior.
  - **I**nterface Segregation: Small, focused protocols/interfaces (e.g., `Sellable` protocol) instead of large ones.
  - **D**ependency Inversion: High-level modules depend on abstractions (e.g., `Inventory` uses abstract `Item` via dependency injection).
- **Themes Covered**:
  - Foundations: Classes, objects, attributes, methods, encapsulation.
  - Intermediate: Inheritance, polymorphism, composition, aggregation.
  - Advanced: Abstract classes, protocols, enums, dataclasses, properties, decorators, context managers, metaclasses, descriptors, weak references, total ordering, monkey-patching (for demo).

## File Structure
To run this project:
1. Create a directory: `ims_project/`
2. Inside it, create `ims_package/` (the package directory).
3. Add the files as shown below.
4. Create a `main.py` at the root to run examples.
5. Install any needed stdlib (no external deps): Run with Python 3.12+.