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

    def test_get_product_prices_multiple(self):

        products = [{'product_id': 1}, {'product_id': 2}, {'product_id': 3}]
        price_list = [
            {'product_id': 1, 'price': 2.50},
            {'product_id': 2, 'price': 3.50},
            {'product_id': 3, 'price': 4.50}
        ]
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

        self.assertEqual(3.50, result[1]["price"])
        self.assertEqual('£', result[1]["currency"])
        self.assertEqual('£3.50', result[1]["price_currency"])
        self.assertEqual(20, result[1]["vat"])
        self.assertEqual(0.70, result[1]["vat_amount"])
        self.assertEqual(4.20, result[1]["total_price"])
        self.assertEqual('£4.20', result[1]["total_price_currency"])

        self.assertEqual(4.50, result[2]["price"])
        self.assertEqual('£', result[2]["currency"])
        self.assertEqual('£4.50', result[2]["price_currency"])
        self.assertEqual(20, result[2]["vat"])
        self.assertEqual(0.90, result[2]["vat_amount"])
        self.assertEqual(5.40, result[2]["total_price"])
        self.assertEqual('£5.40', result[2]["total_price_currency"])

    def test_get_total_price(self):

        products = [{'product_id': 1}, {'product_id': 2}, {'product_id': 3}]
        price_list = [
            {'product_id': 1, 'price': 2.50},
            {'product_id': 2, 'price': 3.50},
            {'product_id': 3, 'price': 4.50}
        ]
        vat = 20
        exchange_rate = {'rate': 1, 'currency': '£'}

        price = Price(products, price_list, vat, exchange_rate)

        result = price.get_total_price()

        self.assertEqual(result['total_price'], 10.50)
        self.assertEqual(result['total_price_currency'], '£10.50')
        self.assertEqual(result['total_price_vat'], 12.60)
        self.assertEqual(result['total_price_vat_currency'], '£12.60')
        self.assertEqual(result['vat'], 20)
