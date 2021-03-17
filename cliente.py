class Cliente:
    def __init__(self, dni, nombre, apellidos):
        self.__dni = dni
        self.__nombre = nombre
        self.__apellidos = apellidos

    def get_dni(self):
        """Devuelve el dni"""
        return self.__dni

    def get_nombre(self):
        """Devuelve el nombre"""
        return self.__nombre

    def get_apellidos(self):
        """Devuelve los apellidos"""
        return self.__apellidos
