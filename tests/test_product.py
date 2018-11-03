import unittest
from price.src.product import Product

class TestProduct(unittest.TestCase):

    def test_product(self):

        product = Product([])

        self.assertIsInstance(product, Product)
