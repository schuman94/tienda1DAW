class Articulo:
    def __init__(self, codigo: int, denominacion: str, precio:int):
        self.__codigo = codigo
        self.__denominacon = denominacion
        self.__precio = precio

    def get_codigo(self):
        """Devuelve el codigo"""
        return self.__codigo

    def get_denominacion(self):
        """ Devuelve al denominacion"""
        return self.__denominacon

    def get_precio(self):
        """Devuelve el precio"""
        return self.__precio
