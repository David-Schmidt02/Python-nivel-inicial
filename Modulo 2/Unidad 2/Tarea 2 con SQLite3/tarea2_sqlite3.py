"""TAREA 2
A partir del ejercicio desafío de la unidad anterior cree una aplicación que permita realizar un alta de registros en la base de datos (sqlite3) """
from tkinter import *
import random
import sqlite3

##INSERCION EN LA BASE
con = sqlite3.connect("mibase.db")


##TK
root = Tk()
root.geometry("350x110")
root.minsize(350, 110)
root.title("Ejercicio Desafio")


def alta():
    global con
    cursor = con.cursor()
    print(pais_e.get(), c_wc_e.get(), posicion_e.get())
    pais1 = pais_e.get()
    wc_1 = c_wc_e.get()
    posicion_1 = posicion_e.get()

    sql = "INSERT INTO futbol(Pais, WC, Posicion) VALUES(?,?,?);"
    datos = (pais1, wc_1, posicion_1)
    cursor.execute(sql, datos)
    con.commit()


# encontré un codigo que permite obtener un color en formato hexadecimal aleatoriamente
def color():
    hexadecimal = ["#" + "".join([random.choice("ABCDEF0123456789") for i in range(6)])]
    root.config(bg=hexadecimal)


pais = StringVar()
c_wc = StringVar()
posicion = StringVar()

label_1 = Label(root, text="Ingrese sus datos", bg="#FADE14", fg="black", anchor=CENTER)
label_1.grid(sticky=W + E, columnspan=4)

pais_e = Entry(root, textvariable=pais)
pais_e.grid(row=1, column=1, sticky=W)
pais_e.config(justify=LEFT)

c_wc_e = Entry(root, textvariable=c_wc)
c_wc_e.grid(row=2, column=1, sticky=W)
c_wc_e.config(justify=LEFT)

posicion_e = Entry(root, textvariable=posicion)
posicion_e.grid(row=3, column=1, sticky=W)
posicion_e.config(justify=LEFT)

label_pais = Label(root, text="País", bg="#01A2FA").grid(row=1, column=0, sticky=W)
label_c_wc = Label(root, text="Campeonatos del Mundo", bg="#01A2FA").grid(
    row=2, column=0, sticky=W
)
label_posicion = Label(root, text="Posición", bg="#01A2FA").grid(
    row=3, column=0, sticky=W
)

boton_alta = Button(root, text="Alta", command=alta).grid(row=4, column=1)
boton_rand_color = Button(root, text="Sorpresa", command=color).grid(row=4, column=2)

root.mainloop()

##lEER LA BASE DE DATOS:
cursor = con.cursor()
sql = "SELECT * FROM futbol"
cursor.execute(sql)
filas = cursor.fetchall()
for x in filas:
    print(x)
