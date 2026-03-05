import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()

ventana.title("Formulario")
ventana.geometry("400x300")

nombre_var = tk.StringVar()
genero_var = tk.StringVar()
lenguaje_var = tk.StringVar()
lenguaje_var.set("seleccione")
pais_var = tk.StringVar()
python = tk.IntVar()
java = tk.IntVar()

label_n = tk.Label(ventana, text="Nombre:").pack()
entry_n = tk.Entry(ventana, textvariable=nombre_var).pack()

label_g = tk.Label(ventana, text="Genero:").pack()
radio_m = tk.Radiobutton(ventana, text="Masculino", variable=genero_var, value="Masculino").pack()
radio_f = tk.Radiobutton(ventana, text="Femenino", variable=genero_var, value="Femenino").pack()    

lable_i = tk.Label(ventana, text= "intereses:").pack()

check_python = tk.Checkbutton(ventana, text= "Python", variable=python).pack()
check_java = tk.Checkbutton(ventana, text= "Java", variable=java).pack()

label_l = tk.Label(ventana, text="Lenguaje de Programacion:").pack()
opcion_m = tk.OptionMenu(ventana, lenguaje_var, "Python", "Java").pack()

label_p = tk.Label(ventana ,text= "seleccione su pais:").pack()
lista_paises = tk.Listbox(ventana, height= 3)
lista_paises.insert(1, "Mexico")
lista_paises.insert(2, "Estados Unidos")       
lista_paises.insert(3, "Canada")
lista_paises.pack()


separador = ttk.Separator(ventana, orient="horizontal").pack(fill="x", pady=10)
label_resultado = tk.Label(ventana, text="resultados").pack()

seccion_resultados = tk.Frame(ventana)
seccion_resultados.pack()

texto = tk.Text(seccion_resultados, height=10, width=40).pack()

scroll = tk.Scrollbar(seccion_resultados, command=texto.yview).pack()
texto.config(yscrollcommand=scroll.set).pack(side= "left").pack(side= "right", fill="y")


def mostrar():
    texto.insert("end", "nombre", + nombre_var.get() + "\n")
    texto.insert("end", "genero", + genero_var.get() + "\n")
    texto.insert("end", "intereses")
    if python.get() == 1:
        texto.insert("end", "Python" + "\n")
    if java.get() == 1:
        texto.insert("end", "Java" + "\n")
    texto.insert("end", "lenguaje de programacion" + lenguaje_var.get() + "\n")
    seleccion = lista_paises.curselection()
    if seleccion:
        texto.insert("end", "pais" + lista_paises.get(seleccion) + "\n")
    texto.insert("end")

boton_mostrar = tk.Button(ventana, text="Mostrar Resultados", command=mostrar).pack()

ventana.mainloop()