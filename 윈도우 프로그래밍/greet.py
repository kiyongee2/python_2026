from tkinter import *

def greet():
    name = entry.get()             # 입력창의 글자 읽기
    result.config(text="안녕하세요, " + name + "님!")  # 라벨 글자 변경

root = Tk()
root.title("인사 프로그램")
root.geometry("260x120")

entry = Entry(root)
entry.pack(padx=10, pady=10)
Button(root, text="인사하기", command=greet).pack()
result = Label(root, text="")      # 결과를 표시할 빈 라벨
result.pack(pady=10)

root.mainloop()