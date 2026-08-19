import tkinter as tk

# 1. 메인 창 생성
root = tk.Tk()
root.title("색상 변경 예제")
root.geometry("300x200")

# [수정 1] 창(root)의 배경색(Background)을 연한 하늘색("lightblue")으로 설정
root.configure(bg="lightblue")

# [수정 2] 라벨 생성 및 옵션 적용
# bg="lightblue": 라벨의 배경색을 창과 맞추어 깔끔하게 보이게 설정
# fg="darkblue": 라벨의 글자색(Foreground)을 진한 파란색으로 설정
# font=("Arial", 12, "bold"): 폰트 종류를 Arial, 크기를 12, 두께를 굵게(bold) 설정
my_label = tk.Label(
    root,
    text="안녕하세요, 파이썬!",
    bg="lightblue",
    fg="darkblue",
    font=("Arial", 12, "bold"),
)

# 라벨을 화면에 배치
my_label.pack(expand=True)

# 이벤트 루프 실행
root.mainloop()