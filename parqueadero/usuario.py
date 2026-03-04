class Usuario:
    def __init__(self,nombre, id, t_usuario):
        self.__nombre = nombre
        self.__id = id
        self.__t_usuario = t_usuario
        
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self,nuevo_nombre):
        if not isinstance (nuevo_nombre, str):
            raise ValueError ("el nombre debe ser texto")
        self.__nombre = nuevo_nombre
        
    def get_id(self):
        return self.__id
    
    def set_id(self, nuevo_id, int):
        if not isinstance (self, nuevo_id):
            raise ValueError("el id debe ser numeros")
        self.__id = nuevo_id
        
    def get_t_usuario(self):
        return self.__t_usuario
    
    def set_t_usuario(self, nuevo_t_usuario):
        self.__t_usuario = nuevo_t_usuario
        
    def mostrar_info(self):
        return f"Id: {self.__id} || Nombre: {self.__nombre} || Tipo de Usuario: {self.__t_usuario}"
        
        