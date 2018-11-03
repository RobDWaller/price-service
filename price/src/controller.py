from price.src.price_list import price_list
from price.src.product import Product
from price.src.price import Price

class Controller:

    @staticmethod
    def read(data):

        product = Product(data['order']['items'])

        price = Price(product.get_products(), price_list, 20, {'rate': 1, 'currency': '£'})

        return {
            'prices': price.get_product_prices(),
            'total': price.get_total_price()
        }
