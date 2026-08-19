import random 
import time

word = ["python", "programming", "challenge", "developer", "algorithm"]

n = 1

print("[타자 게임] 준비되면 엔터를 누르세요!")
input()

start_time = time.time()  # 시작 시간 기록

while n <= 5:
    q = random.choice(word) # 단어 리스트에서 랜덤하게 하나 선택
    print("제시어:", q)
    
    you = input()
    if you == q:
        print("정답입니다!")
        n += 1
    else:
        print("틀렸습니다. 다시 시도하세요.")
    
end_time = time.time()  # 종료 시간 기록
elapsed_time = end_time - start_time  # 경과 시간 계산
# print("게임 종료! 총 걸린 시간: {:.2f}초".format(elapsed_time))
print(f"게임 종료! 총 걸린 시간: {elapsed_time:.2f}초")