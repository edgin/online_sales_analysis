from product import Product
from product_manager import ProductManager
from cart import Cart

manager = ProductManager()
#Create products 
product1 = Product("Laptop", 1, 999.99)
product2 = Product("Monitor", 4, 300)
product3 = Product("Tablet", 3,  399)
product4 = Product("Phone", 3,  299)
product5 = Product("Monitor", 3,  199)
product6 = Product("Mouse", 3,  99)

#Add products to manager_product
manager.add_product(product1)
manager.add_product(product2)
manager.add_product(product3)
<<<<<<< HEAD
=======
manager.add_product(product4)
manager.add_product(product5)
manager.add_product(product6)

#Sum of all products 
manager.product_sum()

#Remove product
>>>>>>> add-cart-functionality
manager.remove_product("Laptop")

#Display all available products
available_products = manager.show_products()
for product in available_products:
    print(f"Product name:{product.name} - product price: {product.price} Quantity: {product.quantity}")

#Add 3 random products to customer cart
random_products = [available_products[0], available_products[2], available_products[4]]
customer_cart_1 = Cart()

for product in random_products:
    print(f"Random product: {product}")
    customer_cart_1.add_product(product)

#Display products in customer cart
customer_cart_1.show_products()

#Sum of all products in customer cart
print(f"Total amount of customer in cart is : {customer_cart_1.total_amount()}")