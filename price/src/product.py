from functools import reduce

class Product:

    def __init__(self, products):

        self.products = products

    def get_products(self):

        def closure(carry, item):

            for i in range(1, (item['quantity'] + 1)):
                carry.append({'product_id': item['product_id']})

            return carry

        return reduce(closure, self.products, [])
