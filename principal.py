from articulo import Articulo
from cliente import Cliente
from factura import Factura
from linea import Linea

#Creamos articulos:
tv = Articulo(1, 'TV SAMSUNG 47 INCH', 399)
grafica = Articulo(2, 'TARJETA GRAFICA NVIDIA', 239)
pen = Articulo(3, 'Pendrive Sandisk 16GB', 12)

#Creamos lineas de compra:
linea1 = Linea(tv, 2)
linea2 = Linea(grafica, 1)
linea3 = Linea(pen, 10)

#Creamos clientes:
rosa = Cliente('45456754J', 'Rosa', 'Gonzalez')
manuel = Cliente('34567421K', 'Manuel', 'Rodriguez')

#Creamos las facturas:
fact1 = Factura(1, rosa, [linea1, linea2])
fact2 = Factura(2, manuel, [linea1, linea2, linea3])

"""
#Trabajamos con las facturas:
fact1.imprimir_factura()
"""
