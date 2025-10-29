

from app.models.customer import Customer
from app.models.invoice  import Invoice
from app.models.item import Item
from app.models.product import Product


#cliente
customer  = Customer("prueba 01", "lastname", "x12345")
#factura

description = input("Ingrese una descripcion de la factura: ")
invoice = Invoice(description, customer )

for __ in range(2):
    name = input("Ingrese un nombre de producto: ")
    price = float(input("Ingrese el precio del producto: "))
    product = Product(name, price)
    
    quantity = int(input("Ingrese la cantidad: "))
    item = Item(quantity, product)
    invoice.add_item(item)

print(invoice.generate_detail())