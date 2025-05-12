class Customer:
    def __init__(self, name):
        self.name = name
        self.order_history = []

    def add_order(self, order):
        self.order_history.append(order)
