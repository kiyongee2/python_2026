
import qrcode

# QR 코드에 담을 데이터
data = "https://www.kaisa.or.kr/"

# QR 코드 생성
img = qrcode.make(data)

# 이미지 저장
img.save("output/qrcode.png")

print("QR 코드가 생성되었습니다!")

