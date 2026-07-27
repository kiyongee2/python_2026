
import qrcode
import tkinter as tk
from tkinter import messagebox

def generate_qr():
    data = entry.get()
    if not data:
        messagebox.showerror("오류", "내용을 입력하세요!")
        return
    
    img = qrcode.make(data)
    img.save("output/qr_gui.png") # output 폴더에 저장(미리 생성 필요)
    messagebox.showinfo("완료", "QR 코드가 생성되었습니다!")

# GUI 생성
window = tk.Tk()
window.title("QR 코드 생성기")

tk.Label(window, text="사이트 URL(http:// 또는 https://):").pack(pady=10)
entry = tk.Entry(window, width=40)
entry.pack(pady=10)

btn = tk.Button(window, text="QR 생성", command=generate_qr)
btn.pack(pady=10)

window.mainloop()

