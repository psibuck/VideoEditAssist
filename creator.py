import tkinter as Tk
from tkinter import *
DIRECTORIES_TO_SPAWN = ["graphics", "audio", "footage"]

window = Tk()

window.title('Hello Python')
window.geometry("300x200+10+20")

for directory in DIRECTORIES_TO_SPAWN:
    Label(window, text=directory).pack(side=TOP)

window.mainloop()
