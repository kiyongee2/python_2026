
import random

# 구구단을 파일로 저장하기
with open('output/word.txt', 'w', encoding='utf-8') as f:
   words =['sky', 'cloud', 'rain', 'sun', 'wind',
           'tree', 'flower', 'mountain', 'river', 'ocean']
   for word in words:
       f.write(f"{word} ")
# 파일 닫기는 with 블록이 끝나면 자동으로 처리됩니다.

# 파일 열기 - 읽기 모드
try:
    with open('output/word.txt', 'r', encoding='utf-8') as f:
        # content = f.read()
        # print(content)
        word = f.read().split() # 공백을 기준으로 단어 분리
        word = random.choice(word) # 랜덤으로 단어 선택
        print(word) # 랜덤으로 선택된 단어 출력
except FileNotFoundError as e:
    print("파일을 찾을 수 없습니다:", e)

