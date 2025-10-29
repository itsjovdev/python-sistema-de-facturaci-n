from invoice.app.models.product import Product


class Item:
    #cantidad de elementos
    def __init__(self, quantity, product: Product | None):
        self.__quantity = quantity
        self.__product = product
        