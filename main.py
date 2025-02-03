from product import Product
from product_manager import ProductManager

manager = ProductManager()

product1 = Product("Laptop", 1, 999.99)
product2 = Product("Monitor", 4, 300)
product3 = Product("Tablet", 3,  399)


manager.add_product(product1)
manager.add_product(product2)
manager.add_product(product3)
manager.remove_product("Laptop")
