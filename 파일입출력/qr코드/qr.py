
import qrcode

data = "http://www.naver.com"

# QR 코드 생성
img = qrcode.make(data)

# QR 코드 이미지 저장
img.save("output/naver_qr.png")
print("QR 코드가 생성되었습니다.")

# QR 코드 이미지 보여주기
img.show()

