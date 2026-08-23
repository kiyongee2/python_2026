"""
tkinter로 만드는 QR 코드 생성기 (초보자용 주석 버전)

동작 방식
1) 입력창(Entry)에 링크(URL)를 입력한다.
2) [생성] 버튼을 누르면 make_qr() 함수가 실행된다.
3) qrcode 라이브러리로 QR 이미지를 만들고 png 파일로 저장한다.
4) 저장한 이미지를 Pillow(PIL)로 다시 열어서 tkinter 창 안에 보여준다.
"""

import os
import tkinter as tk
from tkinter import messagebox

import qrcode
from PIL import ImageTk

# 이 파이썬 파일이 있는 폴더 경로를 구한다.
# -> QR 이미지를 저장할 때 이 폴더 안에 저장하기 위함.
SAVE_DIR = os.path.dirname(os.path.abspath(__file__))


def make_qr():
    """[생성] 버튼을 눌렀을 때 실행되는 함수"""

    # 1. 입력창에서 텍스트를 가져온다. strip()으로 앞뒤 공백을 제거한다.
    link = entry.get().strip()

    # 2. 아무것도 입력하지 않았다면 경고창을 띄우고 함수를 끝낸다.
    if not link:
        messagebox.showwarning("입력 오류", "링크를 입력해 주세요.")
        return

    # 3. qrcode.make()로 QR 코드 이미지를 만든다. (Pillow 이미지 객체가 반환됨)
    img = qrcode.make(link)

    # 4. 만든 이미지를 png 파일로 저장한다.
    save_path = os.path.join(SAVE_DIR, "qr코드.png")
    img.save(save_path)

    # 5. tkinter는 Pillow 이미지를 바로 못 보여주므로
    #    PhotoImage로 변환해야 화면에 표시할 수 있다.
    tk_img = ImageTk.PhotoImage(img.convert("RGB"))

    # 6. 라벨(qr_label)에 이미지를 넣어 화면에 보여준다.
    qr_label.configure(image=tk_img, text="")

    # 7. tk_img를 변수에만 두면 함수가 끝날 때 파이썬 가비지 컬렉터가
    #    이미지를 메모리에서 지워버려서 화면에 이미지가 안 보이게 된다.
    #    그래서 라벨 객체에 직접 붙여서 참조를 계속 유지시킨다.
    qr_label.image = tk_img

    # 8. 저장 경로를 안내 문구로 보여준다.
    status_label.configure(text=f"저장 완료: {save_path}")


# ---------- 화면(GUI) 만들기 ----------

window = tk.Tk()                       # 메인 창 생성
window.title("QR 코드 생성기")           # 창 제목
window.geometry("360x420")             # 창 크기 (가로x세로)
window.resizable(False, False)         # 창 크기 조절 막기

# 안내 문구 라벨
tk.Label(window, text="링크를 입력하세요").pack(pady=(15, 5))

# 링크를 입력받는 입력창
entry = tk.Entry(window, width=40)
entry.pack(pady=5)

# 누르면 make_qr 함수를 실행하는 버튼
tk.Button(window, text="생성", command=make_qr).pack(pady=10)

# QR 이미지를 보여줄 라벨.
# 주의: width/height를 문자(character) 단위로 지정해두면
#       이미지가 들어갈 때도 그 크기 제한이 그대로 적용되어
#       이미지가 매우 작게 잘려 보이는 문제가 생긴다.
#       그래서 크기를 지정하지 않고 이미지 크기에 맞게 자동으로 늘어나게 둔다.
qr_label = tk.Label(window, text="QR 코드가 여기에 표시됩니다")
qr_label.pack(pady=5)

# 저장 경로 등을 안내하는 상태 표시 라벨
status_label = tk.Label(window, text="", fg="gray")
status_label.pack(pady=5)

# 창을 띄우고 이벤트(클릭 등)를 계속 기다린다.
window.mainloop()
