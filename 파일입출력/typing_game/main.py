import random
import time

# 파일에서 단어 읽기
try:
    with open("typing_game/word.txt", "r") as f:
        # strip() 메서드를 사용하여 각 줄의 공백 제거
        word_list = [line.strip() for line in f]  
except FileNotFoundError :
    print("파일이 존재하지 않습니다.")

print("[타자 게임] 준비되면 엔터!")
input()
start = time.time()            # 시작 시간

n = 1
while n <= 5:
    q = random.choice(word_list)
    print("제시어:", q)
    if input() == q:
        print("통과!")
        n += 1
    else:
        print("오타! 다시 도전!")

print(f"게임 종료! 걸린 시간: {time.time()-start:.2f}초")