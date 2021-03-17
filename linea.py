class Linea:
    def __init__(self, articulo, cantidad):
        self.__articulo = articulo
        self.__cantidad = cantidad

    def get_articulo(self):
        """Devuelve el objeto articulo de la linea"""
        return self.__articulo

    def get_cantidad(self):
        """Devuelve la cantidad de veces que se compra el articulo en la linea"""
        return self.__cantidad
