import os
import tkinter as tk
from tkinter import messagebox

import qrcode


OUTPUT_DIR = "output"
DEFAULT_FILE_NAME = "qrcode.png"


def create_qr() -> None:
    data = data_entry.get().strip()
    file_name = file_name_entry.get().strip() or DEFAULT_FILE_NAME

    if not data:
        messagebox.showwarning("입력 오류", "QR 코드에 담을 내용을 입력해 주세요.")
        return

    if not file_name.lower().endswith(".png"):
        file_name += ".png"

    try:
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        file_path = os.path.join(OUTPUT_DIR, file_name)

        img = qrcode.make(data)
        img.save(file_path)

        result_var.set(f"저장 완료: {file_path}")
        messagebox.showinfo("완료", f"QR 코드가 생성되었습니다.\n{file_path}")
    except Exception as exc:
        messagebox.showerror("오류", f"QR 코드 생성 중 문제가 발생했습니다.\n{exc}")


def clear_inputs() -> None:
    data_entry.delete(0, tk.END)
    file_name_entry.delete(0, tk.END)
    file_name_entry.insert(0, DEFAULT_FILE_NAME)
    result_var.set("")


app = tk.Tk()
app.title("QR 코드 생성기")
app.geometry("520x260")
app.resizable(False, False)

main_frame = tk.Frame(app, padx=16, pady=16)
main_frame.pack(fill="both", expand=True)

header_label = tk.Label(main_frame, text="QR 코드 생성기", font=("Malgun Gothic", 16, "bold"))
header_label.pack(anchor="w")

sub_label = tk.Label(main_frame, text="텍스트 또는 URL을 입력하고 QR 코드를 저장하세요.", font=("Malgun Gothic", 10))
sub_label.pack(anchor="w", pady=(4, 14))

input_label = tk.Label(main_frame, text="내용", font=("Malgun Gothic", 10, "bold"))
input_label.pack(anchor="w")

data_entry = tk.Entry(main_frame, font=("Malgun Gothic", 10), width=64)
data_entry.pack(fill="x", pady=(4, 10))
data_entry.insert(0, "https://www.kaisa.or.kr/")

file_label = tk.Label(main_frame, text="파일명 (PNG)", font=("Malgun Gothic", 10, "bold"))
file_label.pack(anchor="w")

file_name_entry = tk.Entry(main_frame, font=("Malgun Gothic", 10), width=64)
file_name_entry.pack(fill="x", pady=(4, 14))
file_name_entry.insert(0, DEFAULT_FILE_NAME)

button_frame = tk.Frame(main_frame)
button_frame.pack(fill="x")

create_button = tk.Button(
    button_frame,
    text="QR 생성",
    font=("Malgun Gothic", 10, "bold"),
    width=12,
    command=create_qr,
)
create_button.pack(side="left")

clear_button = tk.Button(
    button_frame,
    text="초기화",
    font=("Malgun Gothic", 10),
    width=12,
    command=clear_inputs,
)
clear_button.pack(side="left", padx=(8, 0))

result_var = tk.StringVar(value="")
result_label = tk.Label(main_frame, textvariable=result_var, fg="#0a6d0a", font=("Malgun Gothic", 10))
result_label.pack(anchor="w", pady=(16, 0))

app.mainloop()
