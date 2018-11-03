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

    def test_products_two(self):

        products = [
            {'product_id': 1, 'quantity': 2},
            {'product_id': 2, 'quantity': 3},
            {'product_id': 3, 'quantity': 1}
        ]

        product = Product(products)
        result = product.get_products()

        self.assertEqual(len(result), 6)
        self.assertEqual(result[0]['product_id'], 1)
        self.assertEqual(result[1]['product_id'], 1)
        self.assertEqual(result[2]['product_id'], 2)
        self.assertEqual(result[3]['product_id'], 2)
        self.assertEqual(result[4]['product_id'], 2)
        self.assertEqual(result[5]['product_id'], 3)
