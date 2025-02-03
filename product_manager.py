class ProductManager:
    def __init__(self):
        self.products = []       

    def add_product(self, product):
        self.products.append(product)
        print(f"Product '{product.name}' added successfully!")

    def show_products(self):
        return self.products

    def remove_product(self, name):
        filtered_products = []
        for product in self.products:
            if product.name != name:
                filtered_products.append(product)
                print(f"Product '{product.name}' removed successfully!")
            self.products = filtered_products

    def product_sum(self):
        sum_products = sum(product.price * product.quantity for product in self.products)
        print(f"Total sum of products: {float(sum_products)}")
    