import tkinter as tk

def add_numbers():
    # 💡 핵심 포인트: entry.get()과 int()의 관계
    # entry.get()은 사용자가 입력한 값을 무조건 '문자열(텍스트)' 형태로 가져옵니다.
    # 만약 10과 20을 입력했다면, 컴퓨터는 이를 숫자 10이 아니라 글자 "10"과 "20"으로 인식합니다.
    # 문자열끼리 덧셈("10" + "20")을 하면 수학적 계산인 30이 아니라, 글자가 이어 붙여진 "1020"이 되어버립니다.
    # 따라서 올바른 수학적 덧셈을 수행하려면, 글자를 실제 숫자(정수)로 변환해 주는 int() 함수로 반드시 감싸주어야 합니다!
    
    try:
        # 1. 입력창에서 값을 가져와 정수로 변환합니다.
        num1 = int(entry1.get())
        num2 = int(entry2.get())
        
        # 2. 두 숫자를 더합니다.
        result = num1 + num2
        
        # 3. 결과를 라벨에 업데이트합니다.
        label_result.config(text=f"결과: {result}")
        
    except ValueError:
        # (보너스 로직) 사용자가 숫자가 아닌 문자를 입력했을 때 프로그램이 멈추지 않도록 예외를 처리합니다.
        label_result.config(text="결과: 올바른 숫자를 입력하세요!")

# 메인 창 생성 및 설정
window = tk.Tk()
window.title("덧셈 계산기")
window.geometry("300x250") # 창 크기 설정

# 첫 번째 입력창
label1 = tk.Label(window, text="첫 번째 숫자:")
label1.pack(pady=(20, 0))
entry1 = tk.Entry(window)
entry1.pack(pady=5)

# 두 번째 입력창
label2 = tk.Label(window, text="두 번째 숫자:")
label2.pack()
entry2 = tk.Entry(window)
entry2.pack(pady=5)

# [더하기] 버튼 
# command 속성에 함수 이름을 적어주면 버튼 클릭 시 해당 함수가 실행됩니다. (괄호는 쓰지 않습니다)
btn_add = tk.Button(window, text="더하기", command=add_numbers)
btn_add.pack(pady=15)

# 결과 출력 라벨
label_result = tk.Label(window, text="결과: ", font=("Arial", 12, "bold"))
label_result.pack(pady=10)

# GUI 프로그램 실행 (이벤트 루프 시작)
window.mainloop()