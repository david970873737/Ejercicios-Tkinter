class Numero:
    def __init__(self,numero):
        self.__numero = numero

    def get_numero(self):
        return self.__numero

    def set_numero(self, nuevo_numero): 
        if not isinstance(nuevo_numero, (int, float)):
            raise ValueError("no es un numero válido")
        self.__numero = nuevo_numero

    def mostrar_info(self):
        print(f"El número es: {self.__numero}")
