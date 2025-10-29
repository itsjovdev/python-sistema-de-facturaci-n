from datetime import datetime
from typing import List, Optional

from app.models.item import Item
from app.models.customer import Customer

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
    def date(self):
        return self.__date

    @property
    def description(self):
        return self.__description
    
    @property
    def customer(self):
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
    
    #metodo para sumar el precio total de todos los productos(items) que tiene una factura
    def calculate_total(self):
        #creamos la variable total de tipo float, que es donde se almacena el total de los items
        total = 0.00
        #recorremos cada item de la factura y sumamos el valor total de cada uno. 
        #el método item.calculate_amount devuelve el monto total del item(cantidad * precio)
        for item in self.items:
            #total  = sumamos todos esos precios para obtener el total de la factura
            total = total + item.calculate_amount()
        return total 
    
    #metodo que utiliza una expresion generadora: sum( expresión  for variable in colección )
    def calculate_total2(self):
        return sum(item.calculate_amount() for item in self.items)
    
    def generate_detail(self):
        detail = f'Factura nº: {self.folio_id} \n'
        detail = detail + f'Cliente: {self.customer.name} {self.customer.lastname}\t NIF: {self.customer.tax_id}' 
        detail = detail + f'Descripción: {self.description}\n'
        detail = detail + f'Fecha de emision: {self.date.strftime('%d de %B del año %Y')}\n'
        detail = detail + f'Nombre\t$\tCant.\tTotal\n'
        
        for item in self.items:
            detail = detail + f'{item.product.name}\t{item.product.price:.2f}\t{item.quantity}\t{item.calculate_amount():.2f}\n'
        
        detail = detail + f'\nTotal de la factura:  {self.calculate_total():.2f}'
        return detail