from decimal import *

class Price:

    def __init__(self, products, price_list, vat, exchange_rate):

       self.products = products
       self.price_list = price_list
       self.vat = vat
       self.exchange_rate = exchange_rate

    def get_product_prices(self):

        price = self.get_product_price(1)

        return [{
            "price": price,
            "currency": self.exchange_rate['currency'],
            "price_currency": self.exchange_rate['currency'] + '{:.2f}'.format(price),
            "vat": self.vat,
            "vat_amount": (price / 100) * self.vat,
            "total_price": price + ((price / 100) * self.vat),
            "total_price_currency": self.exchange_rate['currency'] + '{:.2f}'.format(price + ((price / 100) * self.vat)),
        }]

    def get_product_price(self, product_id):

        def closure(product):
            return product['product_id'] == product_id

        return list(filter(closure, self.price_list))[0]['price']
