# Atribut: cart_items - lista proizvoda u korpi.
# Metodi:
# dodavanje proizvoda u korpu;
# računanje ukupne vrednosti korpe, tj. iznosa za naplatu;
# prikaz sadržaja korpe.
class Cart:
    def __init__(self):
        self.cart_items = []

    def add_product(self, product):
        print(f"Product type : {type(product)}")
        self.cart_items.append(product)
        print(f"Product '{product.name}' added successfully!")
        
    def total_amount(self):
        return sum(product.price for product in self.cart_items)
    
    def show_products(self):
        print("Show products in cart:")
        for product in self.cart_items:
            print(product.display_info()) 