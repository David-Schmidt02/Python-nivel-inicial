from tkinter import *
import random

root = Tk()
root.geometry("300x110")
root.title("Ejercicio Desafio")


def alta():
    print(titulo_e.get(), ruta_e.get(), desc_e.get())


# encontré un codigo que permite obtener un color en formato hexadecimal aleatoriamente
def color():
    hexadecimal = ["#" + "".join([random.choice("ABCDEF0123456789") for i in range(6)])]
    root.config(bg=hexadecimal)


titulo = StringVar()
ruta = StringVar()
descripcion = StringVar()

label_1 = Label(root, text="Ingrese sus datos", bg="#E800FA", fg="white", anchor=CENTER)
label_1.grid(row=0, column=0, sticky=N)

titulo_e = Entry(root, textvariable=titulo)
titulo_e.grid(row=1, column=1, sticky=W)
titulo_e.config(justify=LEFT)

ruta_e = Entry(root, textvariable=ruta)
ruta_e.grid(row=2, column=1, sticky=W)
ruta_e.config(justify=LEFT)

desc_e = Entry(root, textvariable=descripcion)
desc_e.grid(row=3, column=1, sticky=W)
desc_e.config(justify=LEFT)

label_titulo = Label(root, text="Título", bg="#4CF531").grid(row=1, column=0, sticky=W)
label_ruta = Label(root, text="Ruta", bg="#4CF531").grid(row=2, column=0, sticky=W)
label_descripcion = Label(root, text="Descripción", bg="#4CF531").grid(
    row=3, column=0, sticky=W
)

boton_alta = Button(root, text="Alta", command=alta).grid(row=4, column=1)
boton_rand_color = Button(root, text="Sorpresa", command=color).grid(row=4, column=2)

root.mainloop()
