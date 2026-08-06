from tkinter import *

root = Tk()                       # 1. 기본 창 생성
root.title("첫 GUI 프로그램")         # 2. 창 제목
root.geometry("300x150")          # 3. 창 크기(너비x높이)

Label(root, text="안녕하세요!").pack()   # 4. 라벨 배치
Button(root, text="확인").pack()          # 5. 버튼 배치

root.mainloop()                  # 6. 창 띄우고 대기