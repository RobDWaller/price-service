import unittest
from price.src.product import Product

class TestProduct(unittest.TestCase):

    def test_product(self):

        product = Product([])

        self.assertIsInstance(product, Product)

    def test_products(self):

        products = [
            {'product_id': 1, 'quantity': 2},
            {'product_id': 2, 'quantity': 3}
        ]

        product = Product(products)

        self.assertEqual(len(product.get_products()), 5)
