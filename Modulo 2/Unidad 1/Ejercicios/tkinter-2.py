from tkinter import *


def selec():
    monitor.config(text="Opción {}".format(opcion.get()))


root = Tk()


opcion = IntVar()  # Como StrinVar pero en entero

r_button1 = Radiobutton(root, text="Opción 1", variable=opcion, value=1, command=selec)
r_button1.pack()
r_button2 = Radiobutton(root, text="Opción 2", variable=opcion, value=2, command=selec)
r_button2.pack()
r_button3 = Radiobutton(root, text="Opción 3", variable=opcion, value=3, command=selec)
r_button3.pack()

monitor = Label(root)
monitor.pack()

root.mainloop()
