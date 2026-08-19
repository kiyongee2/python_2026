from tkinter import *

# 1. 용어를 미리 정의 (딕셔너리 자료구조)
words = {
    "CPU": "중앙처리장치. 컴퓨터의 두뇌 역할을 한다.",
    "RAM": "주기억장치. 실행 중인 프로그램이 잠시 저장되는 공간.",
    "GUI": "그래픽 사용자 인터페이스. 버튼·창으로 조작하는 화면.",
    "IP": "인터넷에서 컴퓨터를 구분하는 주소.",
}

def search():
    word = entry.get().strip().upper()      # 입력값(공백 제거, 대문자)
    meaning = words.get(word, "사전에 없는 용어입니다..")  # 없으면 안내문
    output.delete("1.0", END)                # 이전 결과 지우기
    output.insert(END, word + " : " + meaning)  # 결과 출력

root = Tk()
root.title("컴퓨터 용어 사전")
root.geometry("360x220")

entry = Entry(root, width=20)
entry.pack(pady=8)
Button(root, text="검색", command=search).pack()
output = Text(root, width=40, height=6)
output.pack(pady=8)

root.mainloop()