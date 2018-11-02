import unittest
from price.src.price import Price

class TestPrice(unittest.TestCase):

    def test_price(self):

        price = Price([], [], 20, 0);

        self.assertIsInstance(price, Price)
