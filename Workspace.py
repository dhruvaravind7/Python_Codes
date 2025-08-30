from tkinter import *
import random
from tkinter import colorchooser
tk = Tk()
canvas = Canvas(tk, width=1000, height=1000)
canvas.pack()
canvas.create_text(100, 100, text = "My name is Dhruv Aravind", fill = "red", font = ("Times", 10))
tk.mainloop()