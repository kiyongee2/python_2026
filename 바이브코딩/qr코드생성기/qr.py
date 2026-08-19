import qrcode

data = "https://www.python.org"   # QR에 담을 링크/텍스트

img = qrcode.make(data)            # QR 이미지 생성
img.save("my_qr.png")              # 파일로 저장
print("my_qr.png 저장 완료!")