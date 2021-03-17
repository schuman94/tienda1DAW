from cliente import Cliente
from linea import Linea


class Factura:
    def __init__(self, numero, cliente: Cliente, lineas: list):
        """lineas debe ser una lista."""
        self.__numero = numero
        self.__cliente = cliente
        self.__lineas = lineas

    def get_numero(self):
        """Devuelve el numero."""
        return self.__numero

    def get_cliente(self):
        """Devuelve el cliente."""
        return self.__cliente

    def get_lineas(self):
        """Devuelve las lineas."""
        return self.__lineas

    def anyadir_linea(self, linea: Linea):
        """Añade una nueva linea a la factura."""
        self.get_lineas().append(linea)

    def eliminar_linea(self, linea: Linea):
        """
        Elimina la linea indicada. Si hay más de una, se eliminará la más antigua."""
        self.get_lineas().remove(linea)

    def eliminar_ultima_linea(self):
        """Elimina la ultima linea añadida."""
        self.get_lineas().pop()

    def total_factura(self):
        """Devuelve el total de la factura"""
        total = 0
        for i in self.get_lineas():
            precio_articulo = i.get_articulo().get_precio()
            total += precio_articulo * i.get_cantidad()
        return total

    def imprimir_factura(self):
        print(f'Numero de factura: {self.get_numero()}')
        print(f'Cliente: {self.get_cliente()}\n')

        print('Articulo' + '\t\t\t\t' + 'Precio' + '\t\t\t' + 'Cantidad')
        for i in self.get_lineas():
            print(f'{i.get_articulo().get_denominacion()}\t \
                  {i.get_articulo().get_precio()}\t \
                  {i.get_cantidad()}')

        print(f'\nTOTAL: {self.total_factura()} euros')
