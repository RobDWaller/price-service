from functools import reduce

class Price:

    def __init__(self, products, price_list, vat, exchange_rate):

       self.products = products
       self.price_list = price_list
       self.vat = vat
       self.exchange_rate = exchange_rate

    def get_product_prices(self):

        def closure(product):

            price = self.get_product_price(product['product_id'])

            return {
                "price": price,
                "currency": self.exchange_rate['currency'],
                "price_currency": self.exchange_rate['currency'] + '{:.2f}'.format(price),
                "vat": self.vat,
                "vat_amount": round((price / 100) * self.vat, 2),
                "total_price": price + ((price / 100) * self.vat),
                "total_price_currency": self.exchange_rate['currency'] + '{:.2f}'.format(price + ((price / 100) * self.vat)),
            }

        return list(map(closure, self.products))

    def get_product_price(self, product_id):

        def closure(product):
            return product['product_id'] == product_id

        return list(filter(closure, self.price_list))[0]['price']

    def get_total_price(self):

        prices = self.get_product_prices()

        carry = {
            'total_price': 0,
            'total_price_vat': 0,
            'vat': self.vat
        }

        def closure(carry, price):

            carry['total_price'] = carry['total_price'] + price['price']
            carry['total_price_currency'] = price['currency'] + '{:.2f}'.format(carry['total_price'])
            carry['total_price_vat'] = round(carry['total_price_vat'] + price['total_price'], 2)
            carry['total_price_vat_currency'] = price['currency'] + '{:.2f}'.format(carry['total_price_vat'])

            return carry

        return reduce(closure, prices, carry)
