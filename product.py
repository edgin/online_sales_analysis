class Product: 
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = float(price)

    def display_info(self):
        return f"Name: {self.name}, Quantity: {self.quantity}, Price: {self.price}"

    def add_product_info(self, name, price, quantity):
        self.name = name
        self.quantity = quantity
        self.price = price
        print(f"\nProduct information updated successfully: \n name: {name}\n quantity: {quantity}\n price: {price} ")