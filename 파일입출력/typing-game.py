
import random

# 타자 게임
words = ["python", "programming", "typing", "game", "challenge"]

# 랜덤으로 단어 선택
word = random.choice(words)
print("타자 게임에 오신 것을 환영합니다!")
print(f"다음 단어를 입력하세요: {word}")

# 사용자 입력 받기
user_input = input("입력: ")

# 입력한 단어와 선택된 단어 비교
if user_input == word:
    print("정답입니다!")
else:
    print("틀렸습니다. 다시 시도하세요.")