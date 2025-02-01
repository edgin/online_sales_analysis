from product import Product
from product_manager import ProductManager

manager = ProductManager()

product1 = Product("Laptop", 1, 999.99)
product2 = Product("Smartphone", 2, 599.99)
product3 = Product("Tablet", 3,  399)


manager.add_product(product1)
manager.add_product(product2)
manager.add_product(product3)
manager.show_products()
manager.product_sum()
manager.remove_product("Laptop")
