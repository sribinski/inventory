from typing import List
from inventory_types import Product
from inventory_ops import update_price, update_stock
from ui import print_inventory_list, choose_product_index
from storage import load_inventory, save_inventory
import os

os.makedirs("data", exist_ok=True)
FILE_PATH = "data/inventory.json"
try:
    inventory = load_inventory(FILE_PATH)
except ValueError:
    print(f"⚠️  Damaged file: backup created. Initializing with empty database! ")
    inventory = []

def total_items(inventory: List[Product]) -> int:
    return sum(p.stock for p in inventory)

def total_value(inventory: List[Product]) -> float:
    return sum(p.price * p.stock for p in inventory)

def top_by_stock(inventory: List[Product]) -> Product | None:
    if not inventory:
        return None
    return max(inventory, key=lambda p: p.stock)

def top_by_price(inventory: List[Product]) -> Product| None:
    if not inventory:
        return None
    return max(inventory, key=lambda p: p.price)

def show_inventory(inventory: List[Product]) -> None:
    if not inventory:
        print("Inventory is empty.")
        return
    print_inventory_list(inventory, title = "Current Inventory")

def print_report(inventory: List[Product]) -> None:
    if not inventory:
        print("Inventory is empty.")
        return
    print("Inventory Report")
    print("----------------")
    # - Total items
    print(f"Total items in stock: {total_items(inventory)} units")
    # - Total inventory value
    print(f"The total inventory value is ${total_value(inventory):,.2f}")
    # - Top by stock
    top_stock = top_by_stock(inventory)
    print(f"The top by stock is {top_stock.name} ({top_stock.stock:,.0f} units)")
    # - Top by price
    top_price = top_by_price(inventory)
    print(f"The top by price is {top_price.name} (${top_price.price:,.2f})")

def apply_discount(inventory: List[Product],) -> None:
    if not inventory:
        print("Inventory is empty.")
        return    
    print_inventory_list(inventory)
    select_index = choose_product_index(inventory)
    while True:
        try:
            pct = float(input(f"What is the percentage of discount that do you want to apply?: "))
            if pct < 0 or pct > 100:
                print("Percentage must be between 0 and 100!")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    discount = inventory[select_index].price*pct/100
    new_price = inventory[select_index].price - discount
    print(f"The discount for {inventory[select_index].name} is ${discount:.2f}")
    print(f"The final price for {inventory[select_index].name} is ${new_price:,.2f}")
    while True:
        confirmation = input(f"Are you sure to apply {pct}% to {inventory[select_index].name}? (Yes/No): ").strip().lower()
        print()
        if confirmation not in {'yes','no'}:
            print("Please enter 'Yes' or 'No'")
            continue
        break    
    if confirmation == 'yes':
        inventory[select_index].price -= discount

def print_sorted_by_stock(inventory: List[Product]) -> None:
    print("Sorted by stock ")
    print("----------------")
    s= sorted(inventory, key=lambda p: p.stock, reverse=True)
    for p in s:
        print(f"There are {p.stock:,.0f} units of {p.name} for ${p.price:,.2f}")
    print()

def print_sorted_by_price(inventory: List[Product]) -> None:
    print("Sorted by price ")
    print("----------------")
    s= sorted(inventory, key=lambda p: p.price, reverse=True)
    for p in s:
        print(f"There are {p.stock:,.0f} units of {p.name} for ${p.price:,.2f}")

def add_product(inventory: List[Product]) -> None:
    if not inventory:
        print("Inventory is empty.")
        category = input("Enter the new product category: ")
    else:
        print_inventory_list(inventory)
        while True:
            ans = input("Do you want to choose some current category? (Yes/No): ").strip().lower()
            print()
            if ans not in {'yes','no'}:
                print("Please enter 'Yes' or 'No'")
                continue
            break    
        if ans == 'yes':
            select_index = choose_product_index(inventory)
            category = inventory[select_index].category
        elif ans == 'no':
            category = input("Enter the new product category: ")

    while True:
        name = input("Enter the product name: ")
        if any(p.name.lower() == name.lower() for p in inventory):
            print("Product already exists.")
            continue
        break
    while True:
        try:  
            stock = int(input("Enter the amount of this product: "))
            if stock <= 0:
                print("Amount must be positive!")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    while True:    
        try:
            price = float(input("Enter price: "))
            if price <= 0:
                print("Price must be positive!")
                continue
            break
        except ValueError:
            print("Please enter a valid number. Use dot(.) for decimal numbers")
    new_prod = Product(category, name, price, stock)
    inventory.append(new_prod)

def remove_product(inventory: List[Product]) -> None:
    if not inventory:
        print("Inventory is empty.")
        return
    print_inventory_list(inventory)
    select_index = choose_product_index(inventory)
    while True:
        confirmation = input(f"Are you sure to remove {inventory[select_index].name}? (Yes/No): ").strip().lower()
        print()
        if confirmation not in {'yes','no'}:
            print("Please enter 'Yes' or 'No'")
            continue
        break    
    if confirmation == 'yes':
        inventory.pop(select_index)

menu_items= [
    "Show inventory",
    "Add product",
    "Remove product",
    "Update price",
    "Update stock",
    "Report (totals, top by stock/price)",
    "Sort by stock (desc)",
    "Sort by price (desc)",
    "Apply discount (> threshold)",
    ]

while True:
    print("---------------")
    print("Manage the inventory")
    print("---------------")
    for x in range(1,10,1):
        print(f"{x}) {menu_items[x-1]}")
    print("0) Exit")
    print()
    while True:
        try:  
            option = int(input("Please choose the option: "))
            max_option = len(menu_items)
            print()
            if option < 0:
                print("Option must be positive or 0!")
                continue
            elif option > max_option:
                print(f"Please enter option between 1 to {max_option}")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    if option == 0:
        save_inventory(inventory,FILE_PATH)
        exit()
    if option == 1:
        show_inventory(inventory)
    elif option == 2:
        add_product(inventory)
        save_inventory(inventory,FILE_PATH)
    elif option == 3:
        remove_product(inventory)
        save_inventory(inventory,FILE_PATH)
    elif option == 4:
        update_price(inventory)
        save_inventory(inventory,FILE_PATH)
    elif option == 5:
        update_stock(inventory)
        save_inventory(inventory,FILE_PATH)
    elif option == 6:
        print_report(inventory)
    elif option == 7:
        print_sorted_by_stock(inventory)
    elif option == 8:
        print_sorted_by_price(inventory)
    elif option == 9:
        apply_discount(inventory)
        save_inventory(inventory,FILE_PATH)
    print()
    if option != 1:
        while True:
            question = input("Would you like to print the current inventory? (Yes/No): ").strip().lower()
            print()
            if question not in ['yes','no']:
                print("Please enter 'Yes' or 'No'")
                continue
            if question == 'yes':
                show_inventory(inventory)
                print()
            break
    continue
    