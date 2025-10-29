from invoice.app.models.product import Product


class Item:
    # cantidad de elementos
    def __init__(self, quantity, product: Product | None):
        self.__quantity = quantity
        self.__product = product

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        self.__quantity = value

    @property
    def product(self):
        return self.__product

    @product.setter
    def product(self, value):
        self.__product = value
        
    def calculate_amount(self):
        return self.__quantity * self.product.price