class ProductManager:
    def __init__(self):
        self.products = []       

    def add_product(self, product):
        self.products.append(product)
        print(f"Product '{product.name}' added successfully!")


    def show_products(self):
        for product in self.products:
            print(product.display_info())

    def product_sum(self):
        sum_products = sum(product.price * product.quantity for product in self.products)
        print(f"Total sum of products: {float(sum_products)}")
    