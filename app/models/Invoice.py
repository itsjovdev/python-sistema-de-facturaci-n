from datetime import datetime
from typing import List, Optional

from invoice.app.models.item import Item
from invoice.app.models.customer import Customer

class Invoice:
    
    #Creamos un atributo de clase, no de instancia.
    #Esto significa que todas las facturas(Invoice) comparten la misma variable __last_folio.
    #Se usara como contador global para asignar un numero unico a cada factura.
    __last_folio = 0
    
    def __init__(self, description: str, customer: Optional[Customer]):
        #Cada vez que se ejecuta el constructor init, se incrementa el contador global.
        #Esto indica que se ha creado una nueva factura , por lo tanto, el numero de folio aumenta en 1
        Invoice.__last_folio += 1
        
        #El valor del contador (folio) se asigna a la nueva factura que se esta creando.
        # De esta forma, cada factura tiene un numero de folio unico, y esto se genera al crear un objeto del tipo Invoice
        self.__folio_id = Invoice.__last_folio
        
        self.__date = datetime.now()
        self.__description = description
        #factura esta asociado a un cliente
        self.__customer = customer
        #lista
        self.__items: List[Item] = []
        #numero de folio de la factura. solo setter
    
    #Este metodo sirve para obtener el valor del folio_id
    @property
    def folio_id(self):
        return self.__folio_id    

    @property
    def _date(self):
        return self.__date

    @property
    def _description(self):
        return self.__description
    
    @property
    def _customer(self):
        return self.__customer

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
    
    def calculate_total(self):
        total = 0.00
        for item in self.items:
            total = total + item.calculate_amount()
        
        return total 