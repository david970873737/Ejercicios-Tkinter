from usuario import Usuario
from carro import Carro
from parqueadero import Parqueadero
import tkinter as tk

#zona de funciones

parqueadero = Parqueadero()
usuario_actual = None
carro_actual = None

def guardar_info():
    global usuario_actual, carro_actual
    nombre = entrada_usuario.get()
    id_texto = entrada_id.get()
    placa = entrada_carro1.get()
    color = entrada_carro2.get()
    marca = entrada_carro3.get()
    tipo_usuario = entrada_tipo.get()
    
    id_entero = int(id_texto)

    usuario_actual = Usuario(nombre, id_entero, tipo_usuario)
    carro_actual = Carro(placa, color, marca)

    mostrar_usuario = usuario_actual.mostrar_info()
    mostrar_carro = carro_actual.mostrar_info()
    
    etiqueta2.config(text=mostrar_usuario + "\n" + mostrar_carro)
    
    
    
def guardar_puesto():
    global usuario_actual, carro_actual
    
    if usuario_actual is None or carro_actual is None:
        etiqueta.config(text="Primero guarda la información del usuario")
        return
        

    puesto_texto = entrada_puesto.get()
    puesto = int(puesto_texto)

    parqueadero.set_puesto(puesto)
    parqueadero.registrar_Entrada(usuario_actual, carro_actual)
    parqueadero.guardar()
    
    
    mostrar_parqueadero = parqueadero.mostrar_info()

    etiqueta.config(text= mostrar_parqueadero)
    
    
def dar_salida():
    placa = entrada_placa_salida.get()
    mensaje = parqueadero.registrar_salida(placa)
    parqueadero.guardar()
    
    etiqueta3.config(text=mensaje + "\n" + parqueadero.mostrar_info())

ventana = tk.Tk()

ventana.title("Parqueadero")
ventana.geometry("800x400")
ventana.resizable()
titulo = tk.Label(ventana, text= "Parqueadero", font= ( "Courier New", 16),  bg="black", fg= "white")
titulo.pack()

seccion1 = tk.Frame(ventana)
seccion1.pack()

#seccion para ingresar el nombre y el id del usuario
texto_usuario = tk.Label(seccion1, text="Ingrese el nombre del usuario:", font = ("Arial", 12))
texto_usuario.grid(row=0,column=0)
entrada_usuario = tk.Entry(seccion1)
entrada_usuario.grid(row=0, column=1)
texto_usuario = tk.Label(seccion1, text="Ingrese el Id del usuario: ", font=("Ariel",12))
texto_usuario.grid(row=1, column=0)
entrada_id = tk.Entry(seccion1)
entrada_id.grid(row=1, column=1)

#--------------------------------------------------------------------------------------

seccion2 = tk.Frame(ventana)
seccion2.pack()

texto_carro = tk.Label(seccion2, text="Ingrese la placa del usuario:", font=("Arial", 12))
texto_carro.grid(row=0, column=0)
entrada_carro1 = tk.Entry(seccion2)
entrada_carro1.grid(row=0, column=1)
texto_carro = tk.Label(seccion2,text="Ingrese el color del carro del usuario:", font=("Arial", 12))
texto_carro.grid(row=1, column=0)
entrada_carro2 = tk.Entry(seccion2)
entrada_carro2.grid(row=1, column=1)
texto_carro = tk.Label(seccion2,text="Ingrese la marca del carro del usuario:", font=("Arial", 12))
texto_carro.grid(row=2, column=0)
entrada_carro3 = tk.Entry(seccion2)
entrada_carro3.grid(row=2, column=1)
texto_tipo = tk.Label(seccion1, text="Ingrese el tipo de usuario:", font=("Arial", 12))
texto_tipo.grid(row=2, column=0)
entrada_tipo = tk.Entry(seccion1)
entrada_tipo.grid(row=2, column=1)

boton_guardar_info = tk.Button(seccion2, text="Guardar Informacion", command= guardar_info, bg="red")
boton_guardar_info.grid(row=3, column=0, columnspan=2, pady=10)

etiqueta = tk.Label(seccion2 , font=("Arial", 12),wraplength=450, justify="left")
etiqueta.grid(row=4, column=0, columnspan=4)

seccion3 = tk.Frame(ventana)
seccion3.pack()

texto_puesto = tk.Label(seccion3, text= "Ingrese el puesto que desea ocupar:", font= ("Arial", 12))
texto_puesto.grid(row=0,column=0)
entrada_puesto = tk.Entry(seccion3)
entrada_puesto.grid(row=0,column=1)

boton_puesto = tk.Button(seccion3, text= "Guardar Puesto", command=guardar_puesto ,bg = "red")
boton_puesto.grid(row=3, column=0, columnspan=2, pady=10)

etiqueta2 = tk.Label(seccion3, font=  ("Arial", 12))
etiqueta2.grid(row=4, column=0, columnspan=4)



seccion4 = tk.Frame(ventana)
seccion4.pack()

tk.Label(seccion4, text="Placa para salida:", font=("Arial", 12)).grid(row=0, column=0)
entrada_placa_salida = tk.Entry(seccion4)
entrada_placa_salida.grid(row=0, column=1)

boton_salida = tk.Button(seccion4, text="Registrar Salida", command=dar_salida, bg="red")
boton_salida.grid(row=1, column=0, columnspan=2, pady=10)

etiqueta3 = tk.Label(seccion4,font = ("Arial", 12),wraplength=450, justify="left")
etiqueta3.grid(row=4, column=0, columnspan=4)


ventana.mainloop()

