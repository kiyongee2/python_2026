# bmi 계산하기 - 체중(kg)을 키(m)의 제곱으로 나누는 것이며, 단위는 kg/m²

height = float(input("키 입력:"))
weight = float(input("몸무게 입력:"))
height = height / 100 #cm -> m로 변환 

bmi = weight /(height * height)

print(height, weight)
print(f"bmi= {round(bmi, 2)}")

'''
비만 판정 기준 (한국 기준)
저체중: 18.5미만
정상: 18.5 이상 ~ 22.9 이하
과체중: 23 이상 ~ 24.9 이하
비만: 25 이상
'''

if bmi < 18.5:
    print("저체중")
elif bmi >= 18.5 and bmi <= 22.9:
    print("정상")
elif bmi >= 23 and bmi <= 24.9:
    print("과체중")
else:
    print("비만")



