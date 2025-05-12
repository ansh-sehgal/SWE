from customer import Customer
from order_manager import OrderManager
from product_catalogue import ProductCatalogue

def main():
    print("Welcome to AWE Electronics Online Store")
    customer_name = input("Enter your name to continue: ")
    customer = Customer(customer_name)
    catalogue = ProductCatalogue.get_instance()
    order_manager = OrderManager(customer, catalogue)

    while True:
        print("\nMain Menu")
        print("1. View Products")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Place Order")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            catalogue.display_products()
        elif choice == '2':
            product_id = input("Enter Product ID: ")
            qty = int(input("Enter quantity: "))
            order_manager.add_to_cart(product_id, qty)
        elif choice == '3':
            order_manager.view_cart()
        elif choice == '4':
            order_manager.place_order()
        elif choice == '5':
            print("Thank you for visiting AWE Electronics!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
