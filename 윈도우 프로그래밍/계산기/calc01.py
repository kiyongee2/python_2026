import tkinter as tk

# 메인 창 생성
root = tk.Tk()
root.title("4x4 계산기 예제")
root.geometry("250x300")

# 버튼에 들어갈 텍스트 리스트 (4x4 구조)
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", "C", "=", "+"],
]

# 이중 반복문을 사용하여 4x4 격자(grid)에 버튼 배치
for r_idx, row_value in enumerate(buttons):
  for c_idx, btn_text in enumerate(row_value):
    # 각 버튼 생성
    btn = tk.Button(
        root,
        text=btn_text,
        font=("Arial", 14, "bold"),
        width=5,
        height=2,
    )

    # grid()를 이용해 행(row)과 열(column) 지정
    btn.grid(row=r_idx, column=c_idx, padx=5, pady=5)

# 이벤트 루프 실행
root.mainloop()