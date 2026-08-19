from tkinter import *

root = Tk()
root.title("3x3")

n = 1
for r in range(3):
  for c in range(3):
    Button(root, text=str(n), width=5).grid(row=r, column=c, padx=2, pady=2)
    n += 1
    
root.mainloop()