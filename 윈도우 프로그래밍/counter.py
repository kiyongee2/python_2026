from tkinter import *

count = 0
def add():
    global count
    count += 1
    # label.config(text="클릭 횟수: " + str(count))
    label.config(text=f"클릭 횟수: {count}")

root = Tk()
label = Label(root, text="클릭 횟수: 0", font=("맑은 고딕", 14))
label.pack(pady=10)
Button(root, text="누르기", command=add).pack(pady=5)
root.mainloop()