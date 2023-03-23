import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import os

BASE_DIR = os.path.dirname((os.path.abspath(__file__)))
ruta = os.path.join(BASE_DIR, "images.jpeg")

win = Tk()


image2 = Image.open(ruta)
image1 = ImageTk.PhotoImage(image2)

boton = Button(win, image=image1)
boton.pack()

win.mainloop()
