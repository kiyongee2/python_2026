from tkinter import *

root = Tk()
root.title("로그인")
root.geometry("240x120")

Label(root, text="아이디").grid(row=0, column=0, padx=5, pady=5)
Entry(root).grid(row=0, column=1)
Label(root, text="비밀번호").grid(row=1, column=0, padx=5, pady=5)
Entry(root, show="*").grid(row=1, column=1)
Button(root, text="로그인").grid(row=2, column=0, columnspan=2, pady=8)

root.mainloop()