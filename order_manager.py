from shopping_cart import ShoppingCart
from order import Order
from payment_processor import PaymentProcessor

class OrderManager:
    def __init__(self, customer, catalogue):
        self.customer = customer
        self.catalogue = catalogue
        self.cart = ShoppingCart()

    def add_to_cart(self, product_id, quantity):
        product = self.catalogue.get_product(product_id)
        if product and product.stock >= quantity:
            product.reduce_stock(quantity)
            self.cart.add_item(product, quantity)
            print("Item added to cart.")
        else:
            print("Insufficient stock or invalid product ID.")

    def view_cart(self):
        self.cart.show_cart()

    def place_order(self):
        order = Order(self.customer.name, self.cart.items)
        PaymentProcessor.process_payment()
        order.summary()
        self.customer.add_order(order)
        self.cart = ShoppingCart()  # Reset cart after order
