import json
from inventory_types import InventoryItem
from typing import List
from pathlib import Path

def save_inventory(inventory: List[InventoryItem], path: str) -> None:
    with open(path, 'w') as file:
        json.dump(inventory,file,indent=4)

def load_inventory(path: str) -> List[InventoryItem]:
    try:
        with open(path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.decoder.JSONDecodeError:
        original_file = Path(path)
        file_backup = original_file.with_suffix(".json.bak")
        original_file.rename(file_backup)
        raise ValueError(f"CRITICAL ERROR: the file is corruption. Backup created in {file_backup}")