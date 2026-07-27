
import random

# 1~100 사이 랜덤 숫자 생성
answer = random.randint(1, 100)

count = 0  # 시도 횟수

print("🎯 숫자 맞히기 게임 시작!")
print("1부터 100 사이의 숫자를 맞춰보세요.")

while True:
    try:
        user_input = int(input("숫자를 입력하세요: "))
        count += 1

        if user_input > answer:
            print("⬇ 더 작은 숫자입니다.")
        elif user_input < answer:
            print("⬆ 더 큰 숫자입니다.")
        else:
            print(f"🎉 정답입니다! {count}번 만에 맞췄습니다.")
            break

    except ValueError:
        print("⚠️ 숫자만 입력해주세요.")