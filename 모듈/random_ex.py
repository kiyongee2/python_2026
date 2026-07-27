
import random 

print(random.random()) # 0.0 ~ 1.0 사이의 실수 난수 생성

# 시드 설정
random.seed(42)
print(random.random()) # 항상 같은 난수 생성

# 1 ~ 10 사이의 정수 난수 생성
print(random.randint(1, 10)) 

# 동전 던지기
# 0이면 앞면, 1이면 뒷면
coin = random.randint(0, 1)
if coin == 0:
    print("앞면")
else:
    print("뒷면")

# 리스트에서 랜덤하게 하나 선택
print(random.choice(['apple', 'banana', 'cherry'])) 

# 동전 던지기
coin = random.choice(['앞면', '뒷면'])
print(coin)

# 1 ~ 45 사이에서 6개의 고유한 숫자 선택
print(random.sample(range(1, 46), 6))

# 로또 번호 생성
lotto = []
while len(lotto) < 6:
    num = random.randint(1, 45)
    if num not in lotto:
        lotto.append(num)
print("로또 번호:", lotto)
print("로또 번호 (정렬):", sorted(lotto))

