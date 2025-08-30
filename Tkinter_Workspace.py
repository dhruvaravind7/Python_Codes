from tkinter import *
import random
tk = Tk()

canvas = Canvas(tk, width=1500, height=950)
canvas.pack()

def RandomRectangle(width, height):
    x1 = random.randrange(width)
    y1 = random.randrange(height)
    x2 = random.randrange(x1 + width)
    y2 = random.randrange(y1 + height)
    canvas.create_rectangle(x1,y1,x2,y2)

for iter in range(0, 2000):
    RandomRectangle(1500, 950)
