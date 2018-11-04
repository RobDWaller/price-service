'''
Controller module consumes the json product and quantity data and returns
the price information for the products defined.
'''
from price.src.price_list import PRICE_LIST
from price.src.product import Product
from price.src.price import Price

# pylint: disable=too-few-public-methods
class Controller:
    '''
    Controller class includes single static read method to return
    product price information.
    '''

    @staticmethod
    def read(data):
        '''
        Create the product data, pass this to the Price class with the price
        list, the VAT rate and the exchange rate. Return a dict with the
        individual product prices and the total value of all the products.
        '''

        product = Product(data['order']['items'])

        price = Price(
            product.get_products(),
            PRICE_LIST,
            20,
            {'rate': 1, 'currency': '£'}
        )

        return {
            'prices': price.get_product_prices(),
            'total': price.get_total_price()
        }
