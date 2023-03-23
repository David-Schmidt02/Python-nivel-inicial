from tkinter import *
from tkinter import ttk
from tkinter import messagebox as Messagebox
import sqlite3
import re
import datetime


def crear_base():
    con = sqlite3.connect("base_productos.db")
    Messagebox.showwarning("Base de Datos", "Se conectó a la base")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM Productos;")
    lista_tabla = cursor.fetchall()


def crear_tabla():
    con = conexion()
    cursor = con.cursor()
    try:
        sql = "CREATE TABLE Productos(id integer PRIMARY KEY AUTOINCREMENT, Producto text, Laboratorio text, Cantidad integer,Fecha text)"
        cursor.execute(sql)
        con.commit()
        Messagebox.showwarning("Tabla Creada", "Se creó la tabla 'Productos'")
    except:
        Messagebox.showwarning("Error", "La tabla 'Productos' ya fue creada")


def verificar_existencia_tabla(tree):
    con = conexion()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM Productos;")
    lista_tabla = cursor.fetchall()
    if lista_tabla != None:
        actualizar_treeview(tree)


def conexion():
    con = sqlite3.connect("base_productos.db")
    return con


con = conexion()
cursor = con.cursor()


def actualizar_treeview(tree):
    records = tree.get_children()
    for x in records:
        tree.delete(x)
    sql = "SELECT * FROM Productos ORDER BY id ASC"
    con = conexion()
    cursor = con.cursor()
    datos = cursor.execute(sql)
    resultado = datos.fetchall()
    for x in resultado:
        tree.insert("", 0, text=x[0], values=(x[1], x[2], x[3], x[4]))


def alta(tree, p1, l1, c1):
    # regex para el campo cadena
    patron = "^[A-Za-záéíóú]+$"
    if re.match(patron, p1):
        con = conexion()
        cursor = con.cursor()
        fecha = str(datetime.datetime.today().strftime("%d/%m/%y"))
        sql = "INSERT INTO Productos(Producto, Laboratorio, Cantidad,Fecha) VALUES(?,?,?,?);"
        datos = (p1, l1, c1, fecha)
        cursor.execute(sql, datos)
        con.commit()
        Messagebox.showinfo(
            "Alta",
            "Se ha agregado: \nProducto: "
            + p1
            + "\nLaboratorio: "
            + l1
            + "\nCantidad: "
            + c1,
        )
        actualizar_treeview(tree)
    else:
        Messagebox.showwarning("Error", "Error en el campo 'Producto'")


def baja(tree, p1, l1, c1):
    valor = tree.selection()
    resultado = Messagebox.askquestion(
        "Baja", "¿Estas seguro de querer eliminar este producto?"
    )
    if resultado == "yes":
        item = tree.item(valor)
        id_delete = item["text"]
        con = conexion()
        cursor = con.cursor()
        data = (id_delete,)
        sql = "DELETE FROM Productos WHERE id=?;"
        cursor.execute(sql, data)
        con.commit()
        tree.delete(valor)
        Messagebox.showinfo(
            "Eliminado",
            "Se ha eliminado: \nProducto: "
            + p1
            + "\nLaboratorio: "
            + l1
            + "\nCantidad: "
            + c1,
        )
    else:
        Messagebox.showinfo("Acción cancelada", "No se eliminó el producto")


def modificacion(tree, p1, l1, c1):
    valor = tree.selection()
    resultado = Messagebox.askquestion(
        "Baja", "¿Estas seguro de querer modificar este producto?"
    )
    if resultado == "yes":
        item = tree.item(valor)
        id_update = item["text"]
        con = conexion()
        cursor = con.cursor()
        fecha = str(datetime.datetime.today().strftime("%d/%m%y"))
        data = (p1, l1, c1, fecha, id_update)
        sql = "UPDATE Productos SET Producto =?, Laboratorio=?, Cantidad=?,Fecha=? WHERE id = ?;"
        datos = cursor.execute(sql, data)
        con.commit()
        resultado = datos.fetchall()
        for x in resultado:
            tree.insert("", 0, text=x[0], values=(x[1], x[2], x[3]))
        actualizar_treeview(tree)
        Messagebox.showinfo(
            "Modificado",
            "Se ha modificado por: \nProducto: "
            + p1
            + "\nLaboratorio: "
            + l1
            + "\nCantidad: "
            + c1,
        )
    else:
        Messagebox.showinfo("Acción cancelada", "No se modificó el producto")


root = Tk()
root.title("PS COSMÉTICA")
root.resizable(0, 0)
root.config(bg="#F0C266")

# MENU----------------------------------------------------------------
# BASE DE DATOS Y TABLA----------------------------------------------------------------
boton_db = Button(
    root,
    text="Crear Base de Datos",
    bg="#F0C266",
    activebackground="#BD761A",
    command=lambda: crear_base(),
)
boton_db.grid(column=1, row=1, sticky=W, padx=5, pady=2)
boton_table = Button(
    root,
    text="Crear Tabla Productos",
    bg="#F0C266",
    activebackground="#BD761A",
    command=lambda: crear_tabla(),
)
boton_table.grid(column=2, row=1, sticky=W, padx=5, pady=2)

# INGRESO DE DATOS------------------------------------------------------------------------
labe1_p = Label(root, text="Producto:", bg="#F9FFDB")
labe1_p.grid(column=1, row=2, padx=5, pady=5, sticky=W)
combo = ttk.Combobox(
    state="readonly",
    values=[
        "LIDHERMA",
        "EXEL",
        "IDRAET",
        "AP",
        "COLONY",
        "ZINE",
    ],
)
combo.grid(column=2, row=3, padx=5, pady=5, sticky=W)

labe1_l = Label(root, text="Laboratorio:", bg="#F9FFDB")
labe1_l.grid(column=1, row=3, padx=5, pady=5, sticky=W)
labe1_c = Label(root, text="Cantidad:", bg="#F9FFDB")
labe1_c.grid(column=1, row=4, padx=5, pady=5, sticky=W)

producto = StringVar()
laboratorio = StringVar()
cantidad = IntVar()

producto_e = Entry(root, textvariable=producto)
producto_e.grid(column=2, row=2)

cantidad_e = Entry(root, textvariable=cantidad)
cantidad_e.grid(column=2, row=4)

# TREEVIEW------------------------------------------------------------------------
tv = ttk.Treeview(root, columns=("col1", "col2", "col3", "col4"))
tv.column("#0", anchor="w", width=80, minwidth=80)
tv.heading("#0", text="id")
tv.column("col1", anchor="w", width=80, minwidth=80)
tv.heading("col1", text="Producto")
tv.column("col2", anchor="w", width=80, minwidth=80)
tv.heading("col2", text="Laboratorio")
tv.column("col3", anchor="w", width=80, minwidth=80)
tv.heading("col3", text="Cantidad")
tv.column("col4", anchor="w", width=80, minwidth=80)
tv.heading("col4", text="Fecha")
tv.grid(column=0, row=6, columnspan=5)
verificar_existencia_tabla(tv)

# ABCM------------------------------------------------------------------------
boton1 = Button(
    root,
    text="Alta",
    bg="#F0C266",
    activebackground="#BD761A",
    command=lambda: alta(tv, producto_e.get(), combo.get(), cantidad_e.get()),
)
boton1.grid(column=0, row=2, sticky=W, padx=5, pady=2)

boton2 = Button(
    root,
    text="Baja",
    bg="#F0C266",
    activebackground="#BD761A",
    command=lambda: baja(tv, producto_e.get(), combo.get(), cantidad_e.get()),
)
boton2.grid(column=0, row=3, sticky=W, padx=5, pady=2)

boton3 = Button(
    root,
    text="Modificación",
    bg="#F0C266",
    activebackground="#BD761A",
    command=lambda: modificacion(tv, producto_e.get(), combo.get(), cantidad_e.get()),
)
boton3.grid(column=0, row=4, sticky=W, padx=5, pady=2)


root.mainloop()
