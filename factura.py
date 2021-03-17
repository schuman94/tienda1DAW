from linea import Linea


class Factura:
    def __init__(self, numero, cliente, lineas: list):
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

    def get__lineas(self):
        """Devuelve las lineas."""
        return self.__lineas

    def anyadir_linea(self, linea: Linea):
        """Añade una nueva linea a la factura."""
        self.__lineas.append(linea)

    def eliminar_linea(self, linea: Linea):
        """
        Elimina la linea indicada. Si hay más de una, se eliminará la más antigua."""
        self.__lineas.remove(linea)

    def eliminar_ultima_linea(self):
        """Elimina la ultima linea añadida."""
        self.__lineas.pop()
