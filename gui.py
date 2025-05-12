import tkinter as tk
from tkinter import messagebox, simpledialog
from product_catalogue import ProductCatalogue
from customer import Customer
from order_manager import OrderManager

class AWEStoreGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("AWE Electronics Store")
        self.catalogue = ProductCatalogue.get_instance()
        self.customer = Customer("Demo User")
        self.order_manager = OrderManager(self.customer, self.catalogue)
        self.build_main_menu()

    def build_main_menu(self):
        self.clear_window()
        tk.Label(self.root, text="Welcome to AWE Electronics", font=("Arial", 16)).pack(pady=10)
        tk.Button(self.root, text="View Products", command=self.view_products).pack(pady=5)
        tk.Button(self.root, text="Add to Cart", command=self.add_to_cart).pack(pady=5)
        tk.Button(self.root, text="View Cart", command=self.view_cart).pack(pady=5)
        tk.Button(self.root, text="Checkout", command=self.checkout).pack(pady=5)
        tk.Button(self.root, text="Exit", command=self.root.quit).pack(pady=5)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def view_products(self):
        self.clear_window()
        tk.Label(self.root, text="Available Products", font=("Arial", 14)).pack(pady=5)
        for p in self.catalogue.products.values():
            tk.Label(self.root, text=str(p)).pack()
        tk.Button(self.root, text="Back", command=self.build_main_menu).pack(pady=10)

    def add_to_cart(self):
        product_id = simpledialog.askstring("Product ID", "Enter Product ID (e.g., P001):")
        if not product_id:
            return
        quantity = simpledialog.askinteger("Quantity", "Enter Quantity:")
        if quantity is None:
            return
        self.order_manager.add_to_cart(product_id, quantity)

    def view_cart(self):
        self.clear_window()
        tk.Label(self.root, text="Your Cart", font=("Arial", 14)).pack(pady=5)
        cart_items = self.order_manager.cart.items
        if not cart_items:
            tk.Label(self.root, text="Cart is empty.").pack()
        else:
            for item in cart_items.values():
                p = item['product']
                tk.Label(self.root, text=f"{p.name} x {item['quantity']} = ${p.price * item['quantity']}").pack()
            tk.Label(self.root, text=f"Total: ${self.order_manager.cart.calculate_total()}").pack(pady=10)
        tk.Button(self.root, text="Back", command=self.build_main_menu).pack(pady=10)

    def checkout(self):
        if not self.order_manager.cart.items:
            messagebox.showinfo("Checkout", "Cart is empty!")
        else:
            self.order_manager.place_order()
            messagebox.showinfo("Checkout", "Order placed successfully!")
        self.build_main_menu()

if __name__ == "__main__":
    root = tk.Tk()
    app = AWEStoreGUI(root)
    root.mainloop()
