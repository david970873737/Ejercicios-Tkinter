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

    mensaje = parqueadero.registrar_Entrada(usuario_actual, carro_actual)

    etiqueta.config(text=mensaje + "\n" + parqueadero.mostrar_info())
    
    
def dar_salida():
    placa = entrada_placa_salida.get()

    mensaje = parqueadero.registrar_salida(placa)

    etiqueta3.config(text=mensaje + "\n" + parqueadero.mostrar_info())

ventana = tk.Tk()

COLOR_FONDO = "#1e1e2f"
COLOR_SECCION = "#2c2c3e"
COLOR_TITULO = "#ff4c4c"
COLOR_BOTON = "#ff4c4c"
COLOR_TEXTO = "white"

ventana = tk.Tk()
ventana.title("Parqueadero")
ventana.geometry("900x600")
ventana.configure(bg=COLOR_FONDO)


titulo = tk.Label(
    ventana,
    text="PARQUEADERO",
    font=("Segoe UI", 22, "bold"),
    bg=COLOR_TITULO,
    fg="white",
    pady=12
)
titulo.pack(fill="x")

# -------------------------------------------------------

seccion1 = tk.Frame(ventana, bg=COLOR_SECCION, padx=20, pady=20)
seccion1.pack(pady=10)

tk.Label(seccion1, text="Nombre del usuario:", font=("Segoe UI", 11), bg=COLOR_SECCION, fg=COLOR_TEXTO).grid(row=0, column=0, sticky="w")

entrada_usuario = tk.Entry(seccion1, font=("Segoe UI", 11), bd=0)
entrada_usuario.grid(row=0, column=1, padx=10)

tk.Label(seccion1, text="ID del usuario:", font=("Segoe UI", 11), bg=COLOR_SECCION, fg=COLOR_TEXTO).grid(row=1, column=0, sticky="w")

entrada_id = tk.Entry(seccion1, font=("Segoe UI", 11), bd=0)
entrada_id.grid(row=1, column=1, padx=10)

tk.Label(seccion1, text="Tipo de usuario:", font=("Segoe UI", 11), bg=COLOR_SECCION, fg=COLOR_TEXTO).grid(row=2, column=0, sticky="w")

entrada_tipo = tk.Entry(seccion1, font=("Segoe UI", 11), bd=0)
entrada_tipo.grid(row=2, column=1, padx=10)

#-----------------------------------------------------

seccion2 = tk.Frame(ventana, bg=COLOR_SECCION, padx=20, pady=20)
seccion2.pack(pady=10)

tk.Label(seccion2, text="Placa:", font=("Segoe UI", 11),bg=COLOR_SECCION, fg=COLOR_TEXTO).grid(row=0, column=0, sticky="w")

entrada_carro1 = tk.Entry(seccion2, font=("Segoe UI", 11), bd=0)
entrada_carro1.grid(row=0, column=1, padx=10)

tk.Label(seccion2, text="Color:", font=("Segoe UI", 11),bg=COLOR_SECCION, fg=COLOR_TEXTO).grid(row=1, column=0, sticky="w")

entrada_carro2 = tk.Entry(seccion2, font=("Segoe UI", 11), bd=0)
entrada_carro2.grid(row=1, column=1, padx=10)

tk.Label(seccion2, text="Marca:", font=("Segoe UI", 11), bg=COLOR_SECCION, fg=COLOR_TEXTO).grid(row=2, column=0, sticky="w")

entrada_carro3 = tk.Entry(seccion2, font=("Segoe UI", 11), bd=0)
entrada_carro3.grid(row=2, column=1, padx=10)

boton_guardar_info = tk.Button(
    seccion2,
    text="Guardar Información",
    command=guardar_info,
    bg=COLOR_BOTON,
    fg="white",
    font=("Segoe UI", 11, "bold"),
    bd=0,
    padx=12,
    pady=6,
    cursor="hand2",
    activebackground="#ff1a1a"
)

boton_guardar_info.grid(row=3, column=0, columnspan=2, pady=10)

etiqueta = tk.Label(
    seccion2,
    font=("Segoe UI", 11),
    bg=COLOR_SECCION,
    fg="white",
    wraplength=600,
    justify="left"
)
etiqueta.grid(row=4, column=0, columnspan=2)

#_----------------------------------

seccion3 = tk.Frame(ventana, bg=COLOR_SECCION, padx=20, pady=20)
seccion3.pack(pady=10)

tk.Label(seccion3, text="Número de puesto:", font=("Segoe UI", 11), bg=COLOR_SECCION, fg=COLOR_TEXTO).grid(row=0, column=0, sticky="w")

entrada_puesto = tk.Entry(seccion3, font=("Segoe UI", 11), bd=0)
entrada_puesto.grid(row=0, column=1, padx=10)

boton_puesto = tk.Button(
    seccion3,
    text="Registrar Entrada",
    command=guardar_puesto,
    bg=COLOR_BOTON,
    fg="white",
    font=("Segoe UI", 11, "bold"),
    bd=0,
    padx=12,
    pady=6,
    cursor="hand2",
    activebackground="#ff1a1a"
)
boton_puesto.grid(row=1, column=0, columnspan=2, pady=10)

etiqueta2 = tk.Label(
    seccion3,
    font=("Segoe UI", 11),
    bg=COLOR_SECCION,
    fg="white",
    wraplength=600,
    justify="left"
)
etiqueta2.grid(row=2, column=0, columnspan=2)

#---------------------

seccion4 = tk.Frame(ventana, bg=COLOR_SECCION, padx=20, pady=20)
seccion4.pack(pady=10)

tk.Label(seccion4, text="Placa para salida o historial:",
         font=("Segoe UI", 11),
         bg=COLOR_SECCION,
         fg=COLOR_TEXTO).grid(row=0, column=0, sticky="w")

entrada_placa_salida = tk.Entry(seccion4, font=("Segoe UI", 11), bd=0)
entrada_placa_salida.grid(row=0, column=1, padx=10)

boton_salida = tk.Button(
    seccion4,
    text="Registrar Salida",
    command=dar_salida,
    bg=COLOR_BOTON,
    fg="white",
    font=("Segoe UI", 11, "bold"),
    bd=0,
    padx=12,
    pady=6,
    cursor="hand2",
    activebackground="#ff1a1a"
)
boton_salida.grid(row=1, column=0, pady=10)

boton_historial = tk.Button(
    seccion4,text="Ver Historial",command=lambda: etiqueta3.config( text=parqueadero.mostrar_historial(entrada_placa_salida.get())),
    bg="#444",
    fg="white",
    font=("Segoe UI", 11, "bold"),
    bd=0,
    padx=12,
    pady=6,
    cursor="hand2"
)
boton_historial.grid(row=1, column=1, pady=10)

etiqueta3 = tk.Label(
    seccion4,
    font=("Segoe UI", 11),
    bg=COLOR_SECCION,
    fg="white",
    wraplength=700,
    justify="left"
)
etiqueta3.grid(row=2, column=0, columnspan=2)

ventana.mainloop()