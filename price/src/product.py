'''
Product module turns the products and quantiy information in the API supplied
json object into individual product dicts.
'''
from functools import reduce

class Product:
    '''
    Product class contains single end point get products
    '''

    def __init__(self, products):
        '''
        Constructor consumes a list of products and quantity data
        '''

        self.products = products

    def get_products(self):
        '''
        Transforms the products and quantity data into a list of individual
        product dicts. A product with a quantity of 3 will return 3 individual
        product dicts. Returns a list.
        '''

        def closure(carry, item):

            for i in range(1, (item['quantity'] + 1)):
                carry.append({'product_id': item['product_id']})

            return carry

        return reduce(closure, self.products, [])
