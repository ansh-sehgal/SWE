# SWE
AWE electronics store

# AWE Electronics Online Store

This is a simple object-oriented implementation of an online retail system for **AWE Electronics**, built using **Python**.  
It supports basic e-commerce operations through both a **command-line interface (CLI)** and a **graphical user interface (GUI)** built with **Tkinter**.

---

## 🛍️ Features

- View available electronic products (ID, name, price, stock)
- Add products to a shopping cart
- View cart with total price calculation
- Place order with mock payment confirmation
- Both CLI and GUI versions available

---

## 📁 Project Structure

awe_store/
├── main.py # CLI entry point
├── gui.py # GUI application using Tkinter
├── customer.py # Customer class
├── order.py # Order and summary
├── order_manager.py # Controller managing logic
├── payment_processor.py # Mock payment handler
├── product.py # Product class
├── product_catalogue.py # Singleton product listings
├── shopping_cart.py # Cart logic

---

## ▶️ How to Run

### Prerequisites
- Python 3.x (Tkinter is included by default)

### Run the CLI version:

cd awe_store
python main.py

### Run the GUI version:

cd awe_store
python3 gui.py

