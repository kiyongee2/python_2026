from tkinter import *

# 딕셔너리 자료 생성
dic = {
    "변수": "데이터를 저장하기 위한 공간으로, 이름과 값으로 구성됩니다. ",
    "함수": "특정 작업을 수행하는 코드 블록으로, 재사용이 가능하며 입력과 출력을 가질 수 있습니다. ",
    "CPU": "중앙 처리 장치(Central Processing Unit)의 약자로, 컴퓨터의 두뇌에 해당하는 핵심 부품입니다. ",
    "RAM": "임의 접근 메모리(Random Access Memory)의 약자로, 컴퓨터가 작업을 수행하는 동안 데이터를 일시적으로 저장하는 메모리입니다. ",
}


# 검색 버튼을 누르면 입력한 용어의 뜻을 화면에 보여 주는 함수
def search():
    word = entry.get().strip().upper()  # 입력 상자에서 단어를 가져오고 공백을 없앱니다.
    meaning = dic.get(word, "사전에 없는 용어입니다.")  # 딕셔너리에 없으면 안내문을 사용합니다.
    output.delete(1.0, END)  # 이전 검색 결과를 지웁니다.
    output.insert(END, word + " : " + meaning)  # 검색 결과를 출력합니다.


# 새 용어 추가 버튼을 누르면 단어와 뜻을 딕셔너리에 저장하는 함수
def add_word():
    word = add_word_entry.get().strip().upper()  # 검색할 때와 같은 규칙으로 단어를 저장합니다.
    meaning = add_meaning_entry.get().strip()  # 뜻의 앞뒤 공백을 없앱니다.

    # 단어 또는 뜻을 입력하지 않았으면 저장하지 않고 안내합니다.
    if not word or not meaning:
        output.delete(1.0, END)
        output.insert(END, "단어와 뜻을 모두 입력하세요.")
        return

    dic[word] = meaning  # 딕셔너리에 새 용어를 저장합니다. 같은 단어가 있으면 뜻을 바꿉니다.
    add_word_entry.delete(0, END)  # 저장한 뒤 단어 입력칸을 비웁니다.
    add_meaning_entry.delete(0, END)  # 저장한 뒤 뜻 입력칸을 비웁니다.
    output.delete(1.0, END)
    output.insert(END, word + " 용어를 추가했습니다. 이제 검색할 수 있습니다.")


# 메인 윈도우 생성
window = Tk()
window.title("컴퓨터 용어 사전")

# 검색어 입력 레이블과 엔트리(입력상자 - 한 줄)
Label(window, text="용어를 입력하세요:").grid(row=0, column=0, sticky=W, padx=10, pady=5)

entry = Entry(window, width=30)
entry.grid(row=1, column=0, sticky=W, padx=10, pady=5)

# 검색 버튼
Button(window, text="검색", command=search).grid(row=2, column=0, sticky=W, padx=10, pady=5)

# 새 용어와 뜻을 입력하는 상자
Label(window, text="새 용어:").grid(row=3, column=0, sticky=W, padx=10, pady=5)
add_word_entry = Entry(window, width=30)
add_word_entry.grid(row=4, column=0, sticky=W, padx=10, pady=5)

Label(window, text="새 용어의 뜻:").grid(row=5, column=0, sticky=W, padx=10, pady=5)
add_meaning_entry = Entry(window, width=50)
add_meaning_entry.grid(row=6, column=0, sticky=W, padx=10, pady=5)

# 입력한 새 용어를 사전에 저장하는 버튼
Button(window, text="새 용어 추가", command=add_word).grid(row=7, column=0, sticky=W, padx=10, pady=5)

# 결과 출력 텍스트(여러 줄)
output = Text(window, width=50, height=10)
output.grid(row=8, column=0, sticky=W, padx=10, pady=5)

window.mainloop()