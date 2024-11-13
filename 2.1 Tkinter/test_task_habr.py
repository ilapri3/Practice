from tkinter import *
from tkinter import colorchooser
from random import *

size = 600
window = Tk() # создание окна
canvas = Canvas(window, width=size, height=size) # создание холста 600 на 600
canvas.pack() # холст внутри окна
diapason = 0  # далее для цилка

while diapason < 1000:
    colors = choice(['blue', 'green', 'orange', 'pink', 'purple', 'red','yellow'])
    x0 = randint(0, size)
    y0 = randint(0, size)
    d = randint(0, size/5)
    canvas.create_oval(x0, y0, x0+d, y0+d, fill=colors)
    window.update()
    diapason +=1