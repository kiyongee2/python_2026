import qrcode

data = "https://sudo-app.kr/"

img = qrcode.make(data)
img.save("qr코드생성기/sudo-soft.png")
print("qr 이미지 저장 완료!")
