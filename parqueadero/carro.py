class Carro:
    def __init__(self, placa, marca, color):
        self.placa= placa
        self.marca= marca
        self.color= color
        
    def get_placa(self):
        return self.placa
    def get_marca(self):
        return self.marca
    def get_color(self):
        return self.color
    
    def set_placa(self, nueva_placa):
        self.placa= nueva_placa
    def set_marca(self,nueva_marca):
        self.marca= nueva_marca
    def set_color(self, nuevo_color):
        self.color= nuevo_color
        
    def mostrar_info(self):
        return f" -Placa: {self.placa}, -Marca: {self.marca}, -Color: {self.color}"