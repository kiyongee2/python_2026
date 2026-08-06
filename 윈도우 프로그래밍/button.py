from tkinter import *

root = Tk()
root.geometry("260x80")

Button(root, text="왼쪽").pack(side="left", padx=5, pady=10)
Button(root, text="가운데").pack(side="left", padx=5)
Button(root, text="오른쪽").pack(side="left", padx=5)

root.mainloop()