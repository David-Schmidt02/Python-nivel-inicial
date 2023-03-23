from tkinter import *

master = Tk()


def callback():
    print("Hola")


marco = Frame(master)
marco.pack()
marco.config(background="blue")
marco.config(width=5000, height=5000)
marco.config(relief="groove")

b = Button(
    marco,
    text="OK!",
    command=callback,
    anchor=W,
    justify=CENTER,
    padx=22,
    height=30,
    width=12,
)
b.pack()
mainloop()
