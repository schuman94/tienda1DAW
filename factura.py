class Factura:
    def __init__(self, numero, cliente, lineas):
        self.__numero = numero
        self.__cliente = cliente
        self.__lineas = lineas

    def get_numero(self):
        """Devuelve el numero"""
        return self.__numero

    def get_cliente(self):
        """Devuelve el cliente"""
        return self.__cliente

    def get__lineas(self):
        """Devuelve las lineas"""
        return self.__lineas
