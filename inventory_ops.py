from ui import choose_product_index, prompt_new_price, prompt_new_stock
from typing import List, Callable
from inventory_types import Product
from ui import print_inventory_list

def update_price(inventory: List[Product]) -> None:
    if not inventory:
        print("Inventory is empty.")
        return
    _update_numeric_field(inventory,"price",prompt_new_price)

def update_stock(inventory: List[Product]) -> None:
    if not inventory:
        print("Inventory is empty.")
        return
    _update_numeric_field(inventory,"stock",prompt_new_stock)

def _update_numeric_field(inventory: List[Product], field_name: str, prompt_fn: Callable[[str], int | float]) -> None:
    print_inventory_list(inventory)
    select_index = choose_product_index(inventory)
    product_name = inventory[select_index].name
    new_value = prompt_fn(product_name)
    if field_name == "price":
        inventory[select_index].update_price(new_value)
    elif field_name == "stock":
        inventory[select_index].update_stock(new_value)