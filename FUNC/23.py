# Usando una interfaz gráfica
from tkinter import Tk, Label
ventana = Tk()
ventana.title("Hola mundo")
etiqueta = Label(ventana, text="Hola mundo")
etiqueta.pack()
ventana.mainloop()