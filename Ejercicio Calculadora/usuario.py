class Usuario:
    def __init__(self, nombre, id):
        self.__nombre = None
        self.__id = None


    def get_nombre(self):
        return self.__nombre

    def get_id(self):
        return self.__id

    def set_nombre(self, nuevo_nombre):
        if not isinstance(nuevo_nombre, str):
            raise ValueError("El nombre debe ser texto")
        self.__nombre = nuevo_nombre

    def set_id(self, nuevo_id):
        if not isinstance(nuevo_id, int):
            raise ValueError("El ID debe ser entero")
        self.__id = nuevo_id

    def mostrar_info(self):
        print(f"Nombre: {self.__nombre}, ID: {self.__id}")