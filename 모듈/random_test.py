import random

print(random.randint(1, 6))
print(random.choice(['가위', '바위', '보']))

# random.seed(42)
print(random.random())

lotto = []
while len(lotto) < 6:
  n = random.randint(1, 45)
  if n not in lotto:
    lotto.append(n)
print(lotto)

# 랜덤하게 섞기
carts = ['반팔티', '여름바지', '양말']
random.shuffle(carts)
print(carts)

# 숫자 추측 게임
com = random.randint(1, 100)
count = 0
while True:
  you = int(input("1~100 추측: "))
  count += 1
  if you < com:
    print("더 큰수 입력!")
  elif you > com:
    print("더 작은수 입력!")
  else:
    print(f"정답! {count}번 만에 맞혔습니다.")
    break