
from tkinter import *

window = Tk()
window.title("grid 레이아웃")
window.geometry("300x100+100+100")

Button(window, text="동").grid(row=0, column=1)
Button(window, text="서").grid(row=0, column=2)
Button(window, text="남").grid(row=1, column=1)
Button(window, text="북").grid(row=1, column=2)

window.mainloop()