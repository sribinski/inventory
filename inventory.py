from typing import List, Dict

InventoryItem = Dict[str, int | str | float]

inventory: List[InventoryItem] = [
    {"name": "Laptop" , "price": 1500, "stock": 10},
    {"name": "Smartphone", "price": 900.58, "stock": 6},
    {"name": "TV", "price": 400, "stock": 22}
]

def total_items(inventory: List[InventoryItem]) -> int:
    # Total stock sum
    return sum(p["stock"] for p in inventory)

def total_value(inventory: List[InventoryItem]) -> float:
    # Total inventory sum: ∑ price * stock
    return sum(p["price"] * p["stock"] for p in inventory)

def top_by_stock(inventory: List[InventoryItem]) -> InventoryItem:
    # Product with maximum stock
    return max(inventory, key=lambda p: p["stock"])

def top_by_price(inventory: List[InventoryItem]) -> InventoryItem:
    # Product with maximum price
    return max(inventory, key=lambda p: p["price"])

def show_inventory(inventory: List[InventoryItem]) -> None:
    print("Current Inventory")
    print("---------------")
    for i, p in enumerate(inventory, start=1):
        prefix = f"{i}) "
        print(f"{prefix}{p['name']}: {p['stock']:,.0f} units - ${p['price']:,.2f}/unit")

def print_report(inventory: List[InventoryItem]) -> None:
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
    print(f"The top by stock is {top_stock['name']} ({top_stock['stock']:,.0f} units)")
    # - Top by price
    top_price = top_by_price(inventory)
    print(f"The top by price is {top_price['name']} (${top_price['price']:,.2f})")

def apply_discount(inventory: List[InventoryItem], threshold: float = 1000, pct: float = 0.10) -> None:
    # Apply discount if price > threshold
    print("Product discount")
    print("----------------")
    for p in inventory:
        if p["price"] > threshold:
            discount = p['price']*pct
            p["price"] -= discount
            print(f"The discount for {p['name']} is ${discount:.2f}")
            print(f"The final price for {p['name']} is ${p['price']:,.2f}")

def print_sorted_by_stock(inventory: List[InventoryItem]) -> None:
    # Print inventory sorted in descending order by stock
    print("Sorted by stock ")
    print("----------------")
    s= sorted(inventory, key=lambda p: p["stock"], reverse=True)
    for p in s:
        print(f"There are {p['stock']:,.0f} units of {p['name']} for ${p['price']:,.2f}")
    print()

def print_sorted_by_price(inventory: List[InventoryItem]) -> None:
    # Print inventory sorted in descending order by price
    print("Sorted by price ")
    print("----------------")
    s= sorted(inventory, key=lambda p: p["price"], reverse=True)
    for p in s:
        print(f"There are {p['stock']:,.0f} units of {p['name']} for ${p['price']:,.2f}")

def add_product(inventory: List[InventoryItem]) -> None:
    # Add new product
    while True:
        name = input("Enter the product name: ")
        if any(p['name'].lower() == name.lower() for p in inventory):
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
    new_product = {"name": name, "price": price, "stock": stock}
    inventory.append(new_product)

def remove_product(inventory: List[InventoryItem]) -> None:
    # Remove an exist product
    if not inventory:
        print("Inventory is empty.")
        return
    print("Product list")
    print("---------------")
    for i, p in enumerate(inventory, start=1):
        prefix = f"{i}) "
        print(f"{prefix}{p['name']}: {p['stock']:,.0f} units - ${p['price']:,.2f}/unit")
    print()
    while True:
        try:  
            option = int(input("Please choose the product to remove: "))
            max_option = len(inventory)
            if option <= 0:
                print("Option must be positive!")
                continue
            elif option > max_option:
                print(f"Please enter option between 1 to {max_option}")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    op = option-1
    while True:
        confirmation = input(f"Are you sure to remove(Yes/No): {inventory[op]['name']} ").strip().lower()
        print()
        if confirmation not in {'yes','no'}:
            print("Please enter 'Yes' or 'No'")
            continue
        break    
    if confirmation == 'yes':
        inventory.pop(op)

def update_price(inventory: List[InventoryItem]) -> None:
    # Update the price of an existing product
    if not inventory:
        print("Inventory is empty.")
        return
    print("Product list")
    print("---------------")
    for i, p in enumerate(inventory,start=1):
        print(f"{i}) {p['name']}: {p['stock']:,.0f} units - ${p['price']:,.2f}/unit")
    print()
    while True:
        try:  
            option = int(input("Please choose the product to update the price: "))
            max_option = len(inventory)
            if option <= 0:
                print("Option must be positive!")
                continue
            elif option > max_option:
                print(f"Please enter option between 1 to {max_option}")
                continue
            break
        except ValueError:
            print("Please enter a valid number. Use dot(.) for decimal numbers")
    op = option-1
    while True:
        try:  
            new_price = float(input(f"Please enter the new price of {inventory[op]['name']}: "))
            if new_price < 0:
                print("Option must be positive or 0!")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    inventory[op]['price'] = new_price

def update_stock(inventory: List[InventoryItem]) -> None:
    # Update stock of an existing product
    if not inventory:
        print("Inventory is empty.")
        return
    print("Product list")
    print("---------------")
    for i, p in enumerate(inventory, start = 1):
        print(f"{i}) {p['name']}: {p['stock']:,.0f} units - ${p['price']:,.2f}/unit")
    print()
    while True:
        try:  
            option = int(input("Please choose the product to update the stock: "))
            max_option = len(inventory)
            if option <= 0:
                print("Option must be positive!")
                continue
            elif option > max_option:
                print(f"Please enter option between 1 to {max_option}")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    op = option-1
    while True:
        try:  
            new_stock = int(input(f"Please enter the new stock of {inventory[op]['name']}: "))
            break
        except ValueError:
            print("Please enter a valid number.")
    inventory[op]['stock'] = new_stock
# main code
menu_items= [
    "Show inventory",
    "Add product",
    "Remove product",
    "Update price",
    "Update stock (+/-)",
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
        exit()
    if option == 1:
        show_inventory(inventory)
    elif option == 2:
        add_product(inventory)
    elif option == 3:
        remove_product(inventory)
    elif option == 4:
        update_price(inventory)
    elif option == 5:
        update_stock(inventory)
    elif option == 6:
        print_report(inventory)
    elif option == 7:
        print_sorted_by_stock(inventory)
    elif option == 8:
        print_sorted_by_price(inventory)
    elif option == 9:
        apply_discount(inventory)
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

    
