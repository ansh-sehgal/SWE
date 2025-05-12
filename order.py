class Order:
    def __init__(self, customer_name, cart_items):
        self.customer_name = customer_name
        self.cart_items = cart_items

    def summary(self):
        print(f"Order for {self.customer_name}:")
        for item in self.cart_items.values():
            p = item['product']
            print(f"{p.name} x {item['quantity']} = ${p.price * item['quantity']}")
        total = sum(item['product'].price * item['quantity'] for item in self.cart_items.values())
        print(f"Total Paid: ${total}")
