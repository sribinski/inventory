# 🧮 Object-Oriented Inventory Management System (Python CLI)

A robust command-line inventory management program built as part of my self-learning path in Python. 
It focuses on clean logic, Object-Oriented Programming (OOP), data integrity, and modular software architecture.

The project evolved from a simple single-file script using raw dictionaries into a fully modular OOP application with persistent data storage and strict state encapsulation.
---

## 🚀 Features
- **Persistent Storage:** Seamless JSON serialization and deserialization. State is saved locally and reloaded across sessions.
- **Strict Data Integrity:** Core entities are modeled as Python Classes, preventing invalid states (e.g., negative stock or prices).
- Show inventory with formatted terminal output.
- Add / remove products dynamically.
- Update price and stock (protected by class methods).
- Sort by stock (desc) and price (desc) using lambda functions.
- Apply discount above a threshold.
- Summary report: total items, total value, top by stock, top by price.

---

## 🧠 What I Practiced
- **Object-Oriented Programming (OOP):** Classes, Objects, Methods, and the `self` concept.
- **Encapsulation:** Protecting internal state and exposing only safe public methods (`update_price`, `update_stock`).
- **Data Serialization/Deserialization:** Translating raw JSON text into live, intelligent Python Objects (Hydration) and vice versa.
- Advanced Python Built-ins: `sum`, `max`, `sorted` with custom `key` functions.
- Type hints (`typing.List`, `typing.Dict`, `Callable`, union types).
- Error handling (`try/except`) for robust user input validation and file corruption recovery.
- Separation of concerns (UI vs operations vs data vs storage).
- Refactoring techniques and DRY (Don't Repeat Yourself) principles.

---

## 📂 File Structure
- `inventory.py` — Main entry point and menu orchestration.
- `inventory_types.py` — OOP Models: Defines the `Product` class, its state, and encapsulation methods.
- `storage.py` — Persistence Layer: Handles writing to and parsing from JSON files into live objects.
- `inventory_ops.py` — Inventory operations (routing logic to update, add, or remove objects).
- `ui.py` — User interaction helpers (input, print formatting, validation).