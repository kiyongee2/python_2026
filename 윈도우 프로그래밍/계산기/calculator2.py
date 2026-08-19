import tkinter as tk

# -------------------------------
# 버튼을 눌렀을 때 실행되는 함수
# -------------------------------
def add_numbers():
    # Entry.get()은 사용자가 입력한 값을 "문자열(str)" 형태로 가져옵니다.
    # 예를 들어 입력창에 10을 입력해도 "10"이라는 문자열입니다.
    #
    # 문자열끼리 더하면 숫자 계산이 아니라 이어붙이기가 됩니다.
    # 예)
    # "10" + "20" -> "1020"
    #
    # 따라서 숫자 계산을 하려면 int()로 정수형으로 변환해야 합니다.
    num1 = int(entry1.get())
    num2 = int(entry2.get())

    result = num1 + num2

    result_label.config(text=f"결과 : {result}")


# -------------------------------
# 메인 창 생성
# -------------------------------
window = tk.Tk()
window.title("더하기 계산기")
window.geometry("300x180")

# 첫 번째 입력창
tk.Label(window, text="첫 번째 숫자").pack()
entry1 = tk.Entry(window)
entry1.pack()

# 두 번째 입력창
tk.Label(window, text="두 번째 숫자").pack()
entry2 = tk.Entry(window)
entry2.pack()

# 더하기 버튼
add_button = tk.Button(
    window,
    text="더하기",
    command=add_numbers
)
add_button.pack(pady=10)

# 결과 라벨
result_label = tk.Label(window, text="결과 : ")
result_label.pack()

# 프로그램 실행
window.mainloop()