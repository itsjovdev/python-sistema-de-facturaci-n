from datetime import datetime
from typing import List, Optional

from invoice.app.models.item import Item
from invoice.app.models.customer import Customer

class Invoice:
    
    def __init__(self, description: str, customer: Optional[Customer]):
        self.__date = datetime.now()
        self.__description = description
        #factura esta asociado a un cliente
        self.__customer = customer
        #lista
        self.__items: List[Item] = []

    @property
    def _date(self):
        return self.__date

    @_date.setter
    def _date(self, value):
        self.__date = value

    @property
    def _description(self):
        return self.__description

    @_description.setter
    def _description(self, value):
        self.__description = value

    @property
    def _customer(self):
        return self.__customer

    @_customer.setter
    def _customer(self, value):
        self.__customer = value

    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, value):
        self.__items =  value

    
    #Factura tiene sus items
    def add_item(self, item: Item) -> 'Invoice':
        self.__items.append(item)
        return self
    
    