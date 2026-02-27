from usuario import Usuario
from carro import Carro
from datetime import datetime

obj_usuario = Usuario("", "", "")
obj_carro = Carro("", "","")

class Parqueadero:
    def __init__(self):
        self.__puesto = None
        self.__fecha_entrada = None
        self.__h_entrada = None
        self.__h_salida = None
        self.__estado = "Libre"
        self.__usuario = None
        self.__carro = None
        self.__txt_tabla = ""
        
    def get_puesto(self):
        return self.__puesto
    def get_fecha_entrada(self):
        return self.__fecha_entrada
    def get_h_entrada(self):
        return self.__h_entrada  
    def get_h_salida(self):
        return self.__h_salida
    def get_estado(self):
        return self.__estado
    
    def set_puesto(self, nuevo_puesto):
        self.__puesto =  nuevo_puesto    
    def set_estado(self, nueva_estado):
        self.__estado = nueva_estado
        
        
    #=============================================
    
    def registrar_Entrada(self, usuario, carro):
        self.__usuario = usuario
        self.__carro = carro
        hora = datetime.now()
        self.__fecha_entrada = hora.date()
        self.__h_entrada = hora.time()
        self.__estado = "Ocupado"
        
    def registrar_salida(self, placa_buscar):

        if self.__estado == "Ocupado":

            if self.__carro is not None and self.__carro.get_placa() == placa_buscar:

                hora = datetime.now()
                self.__h_salida = hora.time()
                self.__estado = "Libre"

                return "Salida registrada correctamente."

            else:
                return "La placa no coincide."

        else:
            return "El puesto ya está libre."
        
    def guardar(self):
        self.__txt_tabla = self.__txt_tabla + f"Puesto: {self.__puesto} Estado: {self.__estado} || Fecha Entrada: {self.__fecha_entrada} || Hora Entrada: {self.__h_entrada} || Hora Salida: {self.__h_salida}"
        
    def mostrar_info(self):
        return self.__txt_tabla
        
        
    
        