class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, product, quantity):
        if product.product_id in self.items:
            self.items[product.product_id]['quantity'] += quantity
        else:
            self.items[product.product_id] = {'product': product, 'quantity': quantity}

    def calculate_total(self):
        return sum(item['product'].price * item['quantity'] for item in self.items.values())

    def show_cart(self):
        print("\nYour Cart:")
        for item in self.items.values():
            p = item['product']
            print(f"{p.name} x {item['quantity']} = ${p.price * item['quantity']}")
        print(f"Total: ${self.calculate_total()}")
