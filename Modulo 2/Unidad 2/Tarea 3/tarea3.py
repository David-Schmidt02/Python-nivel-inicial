"""TAREA 3
A partir del ejercicio desafío de la unidad anterior cree una aplicación que permita realizar un alta de registros en un archivo de texto (.txt)"""
from tkinter import *
import random

archivo = open("materias.txt", "a")
flag = FALSE
root = Tk()
root.geometry("300x110")
root.title("Ejercicio Desafio")


def alta():
    global archivo
    global flag
    if flag:
        archivo = open("materias.txt", "a")
        archivo.seek(2)
    else:
        flag = TRUE
    string_archivo = (
        str(materia_e.get())
        + "|"
        + str(estado_e.get())
        + "|"
        + str(desc_e.get() + "\n")
    )

    print(string_archivo)
    archivo.write(string_archivo)
    archivo.close()


# encontré un codigo que permite obtener un color en formato hexadecimal aleatoriamente
def color():
    hexadecimal = ["#" + "".join([random.choice("ABCDEF0123456789") for i in range(6)])]
    root.config(bg=hexadecimal)


materia = StringVar()
estado = StringVar()
descripcion = StringVar()

label_1 = Label(root, text="Ingrese sus datos", bg="#E800FA", fg="white", anchor=CENTER)
label_1.grid(row=0, column=0, sticky=N)

materia_e = Entry(root, textvariable=materia)
materia_e.grid(row=1, column=1, sticky=W)
materia_e.config(justify=LEFT)

estado_e = Entry(root, textvariable=estado)
estado_e.grid(row=2, column=1, sticky=W)
estado_e.config(justify=LEFT)

desc_e = Entry(root, textvariable=descripcion)
desc_e.grid(row=3, column=1, sticky=W)
desc_e.config(justify=LEFT)

label_materia = Label(root, text="Materia", bg="#4CF531").grid(
    row=1, column=0, sticky=W
)
label_estado = Label(root, text="Estado", bg="#4CF531").grid(row=2, column=0, sticky=W)
label_descripcion = Label(root, text="Descripción", bg="#4CF531").grid(
    row=3, column=0, sticky=W
)

boton_alta = Button(root, text="Alta", command=alta).grid(row=4, column=1)
boton_rand_color = Button(root, text="Sorpresa", command=color).grid(row=4, column=2)

root.mainloop()

archivo = open("materias.txt", "r")
archivo.seek(0)
for x in archivo:
    print(x, end="")
archivo.close()
