# 🧮 Inventory Management System (Python CLI)

A simple command-line inventory management program built as part of my self-learning path in Python.  
It focuses on clean logic, type hints, modular functions, and user input validation.

The project evolved from a single-file script into a small modular CLI application through refactoring and design improvements.
---

## 🚀 Features
- Show inventory with formatted output
- Add / remove products
- Update price and stock (with validation)
- Sort by stock (desc) and price (desc)
- Apply discount above a threshold
- Summary report: total items, total value, top by stock, top by price

---

## 🧠 What I Practiced
- Core Python: lists, dictionaries, loops, functions
- Built-ins: `sum`, `max`, `sorted`
- Type hints (`typing.List`, `typing.Dict`, union types)
- Error handling and user input validation
- Small, single-responsibility functions
- Working with modular and readable code
- Separation of concerns (UI vs operations vs data)
- Refactoring techniques (extract function, DRY)
- Guard clauses and fail-fast design
- Passing functions as parameters (Callable)

---

## 📂 File Structure
- `inventory.py` — Main entry point and menu orchestration
- `ui.py` — User interaction helpers (input, print, validation)
- `inventory_ops.py` — Inventory operations (update price/stock using shared helpers)
- `inventory_types.py` — Shared type definitions for inventory items
- `storage.py` — Handles data persistence and JSON file operations
