import json
from inventory_types import Product
from typing import List
from pathlib import Path

def save_inventory(inventory: List[Product], path: str) -> None:
    save_list = []
    for p in inventory:
        prod = p.to_dict()
        save_list.append(prod)
    with open(path, 'w') as file:
        json.dump(save_list,file,indent=4)

def load_inventory(path: str) -> List[Product]:
    try:
        with open(path, 'r') as file:
            raw_data = json.load(file)
            new_key = "category"
            for i in raw_data:
                if i.get(new_key) is None:
                    i[new_key] = "none"
            inventory_list = []
            print(raw_data)
            for i in raw_data:
                prod = Product(i['category'],i['name'], i['price'], i['stock'])
                inventory_list.append(prod)
            return inventory_list
    except FileNotFoundError:
        return []
    except json.decoder.JSONDecodeError:
        original_file = Path(path)
        file_backup = original_file.with_suffix(".json.bak")
        original_file.rename(file_backup)
        raise ValueError(f"CRITICAL ERROR: the file is corruption. Backup created in {file_backup}")
