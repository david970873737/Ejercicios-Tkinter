from usuario import Usuario
from calculadora import Calculadora
from numero import Numero
import tkinter as tk

# la funcion la cual se encarga de realizar el calculo
def hacer_calculo():
    try:
        nombre = entrada_usuario.get()
        id_usuario = int(entrada_id.get())

        obj_usuario = Usuario(nombre, id_usuario)

        obj_calculadora = Calculadora(obj_usuario)
        obj_calculadora.set_txt_tabla("")

        operacion_seleccionada = operacion.get()
        obj_calculadora.set_tipo_operacion(operacion_seleccionada)

        n1 = float(entrada_num.get())
        n2 = float(entrada_num2.get())

        numero1 = Numero(n1)
        numero2 = Numero(n2)

        resultado = obj_calculadora.hacer_operacion(numero1, numero2)
        obj_calculadora.set_resultado(resultado)

        etiqueta_resultado.config(text=f"Resultado: {resultado}")

    except ValueError:
        etiqueta_resultado.config(text="Error: Verifique los datos")

#se crea la ventana 
obj_ventana = tk.Tk()
obj_ventana.title("Calculadora")
obj_ventana.geometry("600x600")
obj_ventana.resizable()
titulo = tk.Label(obj_ventana, text="Calculadora", font=("Arial", 16), bg= "black", fg="white")
titulo.pack()

seccion1 = tk.Frame(obj_ventana)
seccion1.pack()

#seccion para ingresar el nombre y el id del usuario
texto_usuario = tk.Label(seccion1, text="Ingrese el nombre del usuario:", font = ("Arial", 12), bg="lightgray", fg="black")
texto_usuario.pack()
entrada_usuario = tk.Entry(seccion1)
entrada_usuario.pack()

texto_usuario = tk.Label(seccion1, text = "Ingrese el Id del Usuario: ", font=("Arial", 12), bg="lightgray", fg="black")
texto_usuario.pack()
entrada_id = tk.Entry(seccion1)
entrada_id.pack()

seccion1.pack(padx=30, pady=30)
#----------------------------------------------------------------------------------------------

seccion2 = tk.Frame(obj_ventana)
seccion2.pack()

#seccion para ingresar los numeros y seleccionar la operacion a realizar
texto_usuario = tk.Label(seccion2, text="Ingrese numero 1: ", font=("Arial", 12), bg="lightgray", fg="black")
texto_usuario.grid(row=0, column=0)
entrada_num = tk.Entry(seccion2)
entrada_num.grid(row=0, column=1)
texto_usuario2 = tk.Label(seccion2, text="Ingrese numero 2: ", font=("Arial", 12), bg="lightgray", fg="black")
texto_usuario2.grid(row=1, column=0)
entrada_num2 = tk.Entry(seccion2)
entrada_num2.grid(row=1, column=1)

operacion = tk.StringVar()
operacion.set("suma")

#seccion para seleccionar la operacion a realizar
tk.Radiobutton(seccion2, text="Suma", variable=operacion, value="suma").grid(row=2, column=0)
tk.Radiobutton(seccion2, text="Resta", variable=operacion, value="resta").grid(row=2, column=1)
tk.Radiobutton(seccion2, text="Multiplicación", variable=operacion, value="multiplicacion").grid(row=2, column=2)
tk.Radiobutton(seccion2, text="División", variable=operacion, value="division").grid(row=2, column=3)

#el boton de calcular
boton_calcular = tk.Button(seccion2, text="Calcular", command=hacer_calculo, font=("Arial", 12), bg="red", fg="white")
boton_calcular.grid(row=3, column=0, columnspan=4, pady=10)

#y aca se muetsra la respuesta 
etiqueta_resultado = tk.Label(seccion2, text = "resultado:" , font=("Arial", 12))
etiqueta_resultado.grid(row=4, column=0, columnspan=4)
obj_ventana.mainloop()