from usuario import Usuario
from datetime import datetime
class Calculadora:
    def __init__(self, user):
        self.__user= user
        self.__tipo_operacion = None
        self.__resultado = None
        self.__fecha = datetime.now()
        self.__txt_tabla = ""

    def get_tipo_operacion(self):
        return self.__tipo_operacion
    
    def set_tipo_operacion(self, nuevo_tipo_operacion):
        self.__tipo_operacion = nuevo_tipo_operacion

    def get_resultado(self):
        return self.__resultado 
    
    def set_resultado(self, nuevo_resultado):
        self.__resultado = nuevo_resultado

    def get_fecha(self):
        return self.__fecha 
    
    def set_fecha(self, nueva_fecha):   
        self.__fecha = nueva_fecha

    def get_txt_tabla(self):
        return self.__txt_tabla
    
    def set_txt_tabla(self, nuevo_txt_tabla):   
        self.__txt_tabla = nuevo_txt_tabla

    def _hacer_suma(self, numero1, numero2):
        self.__resultado = numero1 + numero2
        return self.__resultado
    
    def _hacer_resta(self, numero1, numero2):
        self.__resultado = numero1 - numero2
        return self.__resultado

    def _hacer_multiplicacion(self, numero1, numero2):
        self.__resultado = numero1 * numero2
        return self.__resultado

    def _hacer_division(self, numero1, numero2):
        if numero2 != 0:
            self.__resultado = numero1 / numero2
        else:
            self.__resultado = "Error: División por cero"
        return self.__resultado
    
    def hacer_operacion(self,numero1, numero2):
        if self.__tipo_operacion == "suma":
            return self._hacer_suma(numero1.get_numero(), numero2.get_numero())
        elif self.__tipo_operacion == "resta":
            return self._hacer_resta(numero1.get_numero(), numero2.get_numero())
        elif self.__tipo_operacion == "multiplicacion":
            return self._hacer_multiplicacion(numero1.get_numero(), numero2.get_numero())
        elif self.__tipo_operacion == "division":
            return self._hacer_division(numero1.get_numero(), numero2.get_numero())
        else:
            return "Tipo de operación no válido"
        
    def guardar (self, usuario):
        self.__txt_tabla = self.__txt_tabla + f"{self.__user.get_nombre()} - {self.__tipo_operacion} - {self.__resultado} - {self.__fecha}\n"

    def mostrar_tabla(self):
        print("Tabla de operaciones:")
        print(self.__txt_tabla)

