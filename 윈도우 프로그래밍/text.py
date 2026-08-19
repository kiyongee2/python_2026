import tkinter as tk

window = tk.Tk()
window.title("Text 예제")

# Text: 여러 줄의 긴 내용을 입력받는 위젯
text = tk.Text(window, width=40, height=10)

# 화면에 배치
text.pack()

# 버튼을 클릭하면 입력한 내용을 출력
def show_text():
    # "1.0" = 첫 번째 줄, 첫 번째 글자
    # tk.END = 입력된 내용의 끝
    content = text.get("1.0", tk.END)

    print(content)

button = tk.Button(window, text="내용 확인", command=show_text)
button.pack()

window.mainloop()