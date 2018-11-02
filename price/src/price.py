from decimal import *

class Price:

    def __init__(self, products, price_list, vat, exchange_rate):

       self.products = products
       self.price_list = price_list
       self.vat = vat
       self.exchange_rate = exchange_rate

    def get_product_prices(self):

        return [{
            "price": 2.50,
            "currency": self.exchange_rate['currency'],
            "price_currency": self.exchange_rate['currency'] + '{:.2f}'.format(2.50),
            "vat": self.vat,
            "vat_amount": (2.50 / 100) * self.vat,
            "total_price": 2.50 + ((2.50 / 100) * self.vat),
            "total_price_currency": self.exchange_rate['currency'] + '{:.2f}'.format(2.50 + ((2.50 / 100) * self.vat)),
        }]
