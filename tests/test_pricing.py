import unittest
from price.src.price import Price

class TestPrice(unittest.TestCase):

    def test_price(self):

        price = Price();

        self.assertIsInstance(price, Price)
