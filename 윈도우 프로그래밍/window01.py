
from tkinter import *

# 버튼 클릭 이벤트 핸들러
def click():
  # print("Button Clicked!")
  output.config(text="Button Clicked!")

root = Tk()
root.title("윈도우 프로그래밍")
root.geometry("250x100+100+100")

# 라벨과 버튼 추가
Label(root, text="Hello, World!").pack()
Button(root, text="Click Me!", command=click).pack()

# 클릭 후 출력 라벨
output = Label(root, text="")
output.pack()

root.mainloop()