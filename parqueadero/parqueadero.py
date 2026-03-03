from datetime import datetime

class Parqueadero:
    def __init__(self):
        self.__historial = []
        self.__puesto = None
        self.__fecha_entrada = None
        self.__h_entrada = None
        self.__h_salida = None
        self.__estado = "Libre"
        self.__puestos_ocupados = {}

    # =============================
    # GETTERS
    # =============================

    def get_puesto(self):
        return self.__puesto

    def get_estado(self):
        return self.__estado

    # =============================
    # SETTERS
    # =============================

    def set_puesto(self, nuevo_puesto):
        self.__puesto = nuevo_puesto

    def set_estado(self, nuevo_estado):
        self.__estado = nuevo_estado

    # =============================
    # REGISTRAR ENTRADA
    # =============================

    def registrar_Entrada(self, usuario, carro):

        if self.__puesto in self.__puestos_ocupados:
            return "Ese puesto ya está ocupado"

        hora = datetime.now()
        self.__fecha_entrada = hora.date()
        self.__h_entrada = hora
        self.__estado = "Ocupado"

        registro = {
            "placa": carro.get_placa(),
            "usuario": usuario.get_nombre(),
            "puesto": self.__puesto,
            "fecha_entrada": self.__fecha_entrada,
            "hora_entrada": self.__h_entrada,
            "hora_salida": None
        }

        self.__historial.append(registro)
        self.__puestos_ocupados[self.__puesto] = carro.get_placa()

        return "Entrada registrada correctamente"



    def registrar_salida(self, placa):

        for registro in self.__historial:
            if registro["placa"] == placa and registro["hora_salida"] is None:

                self.__h_salida = datetime.now()
                registro["hora_salida"] = self.__h_salida

                puesto = registro["puesto"]

                if puesto in self.__puestos_ocupados:
                    del self.__puestos_ocupados[puesto]

                self.__estado = "Libre"

                return "Salida registrada correctamente"

        return "No se encontró un carro activo con esa placa"


    def mostrar_historial(self, placa):

        texto = ""

        for registro in self.__historial:
            if registro["placa"] == placa:
                texto += f"""
                        Placa: {registro['placa']}
                        Usuario: {registro['usuario']}
                        Puesto: {registro['puesto']}
                        Entrada: {registro['fecha_entrada']} {registro['hora_entrada']}
                        Salida: {registro['hora_salida']}
                        -------------------------
                        """

        if texto == "":
            return "No hay historial para esa placa"

        return texto

    

    def mostrar_info(self):

        if not self.__puestos_ocupados:
            return "No hay puestos ocupados"

        texto = ""

        for puesto, placa in self.__puestos_ocupados.items():
            texto += f"Puesto {puesto} -> Placa: {placa}\n"

        return texto