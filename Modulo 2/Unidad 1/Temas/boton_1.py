from tkinter import *
from tkinter.filedialog import askopenfile
from tkinter import filedialog as FileDialog

master = Tk()


def callback():
    ruta = askopenfile(title="Busca gato")
    print(ruta)


def callback2():
    ruta = FileDialog.askopenfilename(title="Busca gato")
    print(ruta)


b = Button(master, text="Abrir", justify=RIGHT, command=callback, bg="blue", fg="white")
b.grid(row=10, column=10)


c = Button(master, text="Abrir", justify=RIGHT, command=callback2, bg="green", fg="red")
c.grid(row=20, column=10)


mainloop()
