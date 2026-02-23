
class Product:
    def __init__(self, name: str, price: float, stock: int):
        self.name = name
        self.price = price
        self.stock = stock
    def update_stock(self, new_stock: int):
        if new_stock >= 0:
            self.stock = new_stock
    def update_price(self, new_price: float):
        if new_price > 0:
            self.price = new_price
    def to_dict(self) -> dict:
        return {"name": self.name, "price": self.price, "stock": self.stock}