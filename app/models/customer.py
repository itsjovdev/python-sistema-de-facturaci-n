class Customer:
    def __init__(self, name: str, lastname: str, tax_id: str):
        self.__name = name
        self.__lastname = lastname
        self.__tax_id = tax_id

    @property
    def _name(self):
        return self.__name

    @_name.setter
    def _name(self, value):
        self.__name = value

    @property
    def _lastname(self):
        return self.__lastname

    @_lastname.setter
    def _lastname(self, value):
        self.__lastname = value

    @property
    def _tax_id(self):
        return self.__tax_id
