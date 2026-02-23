from typing import List
from inventory_types import Product

def choose_product_index(inventory: List[Product]) -> int:
    max_choice = len(inventory)
    while True:
        try:  
            choice = int(input(f"Please choose the product: "))
            if choice <= 0 or choice > max_choice:
                print(f"Please enter a number between 1 and {max_choice}")
                continue
            break
        except ValueError:
            print("Please enter a whole number.")
    index = choice-1
    return index

def prompt_new_price(product_name: str) -> float:
    while True:
        try:  
            new_price = float(input(f"Please enter the new price of {product_name}: "))
            if new_price < 0:
                print("Price must be positive or 0!")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    return new_price

def prompt_new_stock(product_name: str) -> int:
    while True:
        try:  
            new_stock = int(input(f"Please enter the new stock of {product_name}: "))
            if new_stock < 0:
                print("Stock must be 0 or greater!")
                continue
            break
        except ValueError:
            print("Please enter a whole number.")
    return new_stock

def print_inventory_list(inventory: List[Product], title: str = "Product List") -> None:
    if not inventory:
        print("Inventory is empty.")
        return
    print(title)
    print("---------------")
    for i, p in enumerate(inventory, start=1):
        prefix = f"{i}) "
        print(f"{prefix}{p.name}: {p.stock:,.0f} units - ${p.price:,.2f}/unit")
    print()