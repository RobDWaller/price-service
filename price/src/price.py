'''
Price module calculates the values of the individual products and the total
value of all the products.
'''
from functools import reduce

class Price:
    '''
    Price class includes two main methods, get product prices returns the
    value of each individual product and get total price returns the value
    of all the products.
    '''

    def __init__(self, products, price_list, vat, exchange_rate):
        '''
        Constructor consumes a list of products, the price list, the VAT rate
        and the exchange rate dict.
        '''

        self.products = products
        self.price_list = price_list
        self.vat = vat
        self.exchange_rate = exchange_rate

    def get_product_prices(self):
        '''
        Return the value of each individual product. Maps the product data to
        calculate base cost of product along with the product plus VAT
        '''

        def closure(product):

            price = self.get_product_price(product['product_id'])

            return {
                "price": price,
                "currency": self.exchange_rate['currency'],
                "price_currency": self.exchange_rate['currency'] + '{:.2f}'.format(price),
                "vat": self.vat,
                "vat_amount": round((price / 100) * self.vat, 2),
                "total_price": price + ((price / 100) * self.vat),
                "total_price_currency": self.exchange_rate['currency'] + '{:.2f}'.format(
                    price + ((price / 100) * self.vat)
                )
            }

        return list(map(closure, self.products))

    def get_total_price(self):
        '''
        Reduces all the product value data into a single dict which represents
        the total value of all the products added together.
        '''

        prices = self.get_product_prices()

        carry = {
            'total_price': 0,
            'total_price_vat': 0,
            'vat': self.vat
        }

        def closure(carry, price):

            carry['total_price'] = carry['total_price'] + price['price']
            carry['total_price_currency'] = price['currency'] + '{:.2f}'.format(
                carry['total_price']
            )
            carry['total_price_vat'] = round(
                carry['total_price_vat'] + price['total_price'], 2
            )
            carry['total_price_vat_currency'] = price['currency'] + '{:.2f}'.format(
                carry['total_price_vat']
            )

            return carry

        return reduce(closure, prices, carry)

    def get_product_price(self, product_id):
        '''
        Find the product price from the price list based on the product id
        '''

        def closure(product):
            return product['product_id'] == product_id

        price = list(filter(closure, self.price_list))[0]['price']

        return round(price * self.exchange_rate['rate'], 2)
