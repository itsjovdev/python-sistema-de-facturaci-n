class Product: 

    def __init__(self, name: str, price: float):
        self.__name = name
        self.__price = price

    @property
    def _name(self):
        return self.__name

    @_name.setter
    def _name(self, value):
        self.__name = value

    @property
    def _price(self):
        return self.__price

    @_price.setter
    def _price(self, value):
        self.__price = value
