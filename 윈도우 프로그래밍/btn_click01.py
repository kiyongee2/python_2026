from tkinter import *

def click():                 # 버튼을 누르면 실행될 함수
    print("버튼이 눌렸습니다!")

root = Tk()

Button(root, text="확인", command=click).pack(padx=20, pady=20)
# command=click  → 괄호 없이! 클릭할 때 실행
root.mainloop()