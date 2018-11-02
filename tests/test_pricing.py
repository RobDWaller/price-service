import unittest
from price.src.price import Price

class TestPrice(unittest.TestCase):

    def test_price(self):

        price = Price([], [], 20, 0);

        self.assertIsInstance(price, Price)

    def test_get_product_prices(self):

        products = [{'product_id': 1}]
        price_list = [{'product_id': 1, 'price': 2.50}]
        vat = 20
        exchange_rate = {'rate': 1, 'currency': '£'}

        price = Price(products, price_list, vat, exchange_rate)

        result = price.get_product_prices()

        self.assertEqual(2.50, result[0]["price"])
        self.assertEqual('£', result[0]["currency"])
        self.assertEqual('£2.50', result[0]["price_currency"])
        self.assertEqual(20, result[0]["vat"])
        self.assertEqual(0.50, result[0]["vat_amount"])
        self.assertEqual(3.00, result[0]["total_price"])
        self.assertEqual('£3.00', result[0]["total_price_currency"])

    def test_get_product_price(self):

       products = [{'product_id': 1}]
       price_list = [{'product_id': 1, 'price': 2.50}]
       vat = 20
       exchange_rate = {'rate': 1, 'currency': '£'}

       price = Price(products, price_list, vat, exchange_rate)

       self.assertEqual(2.50, price.get_product_price(1))

    def test_get_product_price_two(self):

        products = [{'product_id': 2}]
        price_list = [{'product_id': 2, 'price': 3.50}]
        vat = 20
        exchange_rate = {'rate': 1, 'currency': '£'}

        price = Price(products, price_list, vat, exchange_rate)

        self.assertEqual(3.50, price.get_product_price(2))
