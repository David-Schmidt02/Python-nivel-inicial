from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import os

BASE_DIR = os.path.dirname((os.path.abspath(__file__)))
ruta = os.path.join(BASE_DIR, "images.jpeg")

root = Tk()
root.geometry("700x470")
photo = ImageTk.PhotoImage(file=ruta)
label = Label(root, image=photo)
label.place(x=0, y=0)
root.mainloop()
