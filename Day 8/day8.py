class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print("Product Details: ")
        print("Name: ", self.name)
        print("Price: ", self.price)
        print("Quantity: ", self.quantity)

    def product_registration():
        name = input("Enter product name: ")
        price = input("Enter product price: ")
        quantity = input("Enter product quantity: ")

        new_product = Product(name, price, quantity)
        product_db.append(new_product)
        print("Product created successfully")
product_db = []

Product.product_registration()