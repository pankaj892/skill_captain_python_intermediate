# Python code for the Cart class

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print("Name: ", self.name)
        print("Price: ", self.price)
        print("Quantity: ", self.quantity)

class Cart:
    def __init__(self, name):
        self.product_list = []
        self.name = name

    def add_to_cart(self, product):
        self.product_list.append(product)

    def remove_from_cart(self, product_name):
        for product in self.product_list:
            if product.name == product_name:
                self.product_list.remove(product)
                print("Product removed successfully")
                return
        print("Product not found")

    def display_cart(self):
        if len(self.product_list) <= 0:
            raise ValueError("Cart is empty")
            return
        else:
            print("Cart Details: ")
            print("Name: ", self.name)
            for product in self.product_list:
                product.display_info()


# Test the functionality of the Cart class
def test_cart():
    product1 = Product("Shirt", 19.99, 2)
    product2 = Product("Jeans", 29.99, 1)
    product3 = Product("Shoes", 49.99, 1)

    cart = Cart("John Doe")
    cart.add_to_cart(product1)
    cart.add_to_cart(product2)
    cart.add_to_cart(product3)

    cart.display_cart()

    cart.remove_from_cart("Shirt")
    cart.display_cart()


test_cart()