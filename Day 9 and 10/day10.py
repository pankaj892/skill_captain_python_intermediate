# Test Cases for the Cart class

import unittest
from day9 import Cart, Product

class TestCart(unittest.TestCase):
    def setUp(self):
        self.product1 = Product("Shirt", 19.99, 2)
        self.product2 = Product("Jeans", 29.99, 1)
        self.product3 = Product("Shoes", 49.99, 1)

        self.cart = Cart("John Doe")
        self.cart.add_to_cart(self.product1)
        self.cart.add_to_cart(self.product2)
        self.cart.add_to_cart(self.product3)

    def test_add_to_cart(self):
        self.assertEqual(len(self.cart.product_list), 3)
        self.cart.add_to_cart(Product("Socks", 9.99, 3))
        self.assertEqual(len(self.cart.product_list), 4)

    def test_remove_from_cart(self):
        self.cart.remove_from_cart("Shirt")
        self.assertEqual(len(self.cart.product_list), 2)
        self.cart.remove_from_cart("Jeans")
        self.assertEqual(len(self.cart.product_list), 1)
        self.cart.remove_from_cart("Shoes")
        self.assertEqual(len(self.cart.product_list), 0)

    def test_display_cart(self):
        self.cart.remove_from_cart("Shirt")
        self.cart.display_cart()
        self.cart.remove_from_cart("Jeans")
        self.cart.display_cart()
        self.cart.remove_from_cart("Shoes")
        self.cart.display_cart()

if __name__ == "__main__":
    unittest.main()
