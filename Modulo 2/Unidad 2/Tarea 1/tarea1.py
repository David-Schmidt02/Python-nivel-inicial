"""TAREA 1
A partir del ejercicio desafío de la unidad anterior cree una aplicación que permita realizar un alta de registros en un diccionario dentro de la app"""

from tkinter import *
import random
import shelve

root = Tk()
root.geometry("300x110")
root.title("Ejercicio Desafio")

id = "0"
diccionario = {}


def alta():
    db = shelve.open("productos")
    global id
    print("Usted guardo: ", fruta_e.get(), cantidad_e.get(), precio_e.get())
    id = str(int(id) + 1)
    diccionario = {
        "Titulo": fruta_e.get(),
        "Ruta": cantidad_e.get(),
        "Descripción": precio_e.get(),
    }
    db[id] = diccionario
    db.close()


# encontré un codigo que permite obtener un color en formato hexadecimal aleatoriamente
def color():
    hexadecimal = ["#" + "".join([random.choice("ABCDEF0123456789") for i in range(6)])]
    root.config(bg=hexadecimal)


fruta = StringVar()
cantidad = StringVar()
precio = StringVar()

label_1 = Label(root, text="Ingrese sus datos", bg="#FADE14", fg="black", anchor=CENTER)
label_1.grid(row=0, column=0, sticky=W + E, columnspan=4)

fruta_e = Entry(root, textvariable=fruta)
fruta_e.grid(row=1, column=1, sticky=W)
fruta_e.config(justify=LEFT)

cantidad_e = Entry(root, textvariable=cantidad)
cantidad_e.grid(row=2, column=1, sticky=W)
cantidad_e.config(justify=LEFT)

precio_e = Entry(root, textvariable=precio)
precio_e.grid(row=3, column=1, sticky=W)
precio_e.config(justify=LEFT)

label_titulo = Label(root, text="Fruta", bg="#FADE14").grid(row=1, column=0, sticky=W)
label_ruta = Label(root, text="Cantidad", bg="#FADE14").grid(row=2, column=0, sticky=W)
label_descripcion = Label(root, text="Precio", bg="#FADE14").grid(
    row=3, column=0, sticky=W
)

boton_alta = Button(root, text="Alta", command=alta).grid(row=4, column=1)
boton_rand_color = Button(root, text="Sorpresa", command=color).grid(row=4, column=2)

root.mainloop()

db = shelve.open("productos")
for key in db:
    print(key, "==>", db[key]["Titulo"], db[key]["Ruta"], db[key]["Descripción"])
db.close()
