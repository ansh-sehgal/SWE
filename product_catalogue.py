from product import Product

class ProductCatalogue:
    _instance = None

    @staticmethod
    def get_instance():
        if ProductCatalogue._instance is None:
            ProductCatalogue()
        return ProductCatalogue._instance

    def __init__(self):
        if ProductCatalogue._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            ProductCatalogue._instance = self
            self.products = {
                "P001": Product("P001", "Laptop", 1200, 10),
                "P002": Product("P002", "Smartphone", 800, 15),
                "P003": Product("P003", "Headphones", 150, 20)
            }

    def get_product(self, product_id):
        return self.products.get(product_id)

    def display_products(self):
        for p in self.products.values():
            print(p)
