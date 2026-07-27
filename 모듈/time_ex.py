
import time

print("현재 시간:", time.time()) #1775224469.4519815
print("현재 시간 (로컬):", time.localtime())
print(time.ctime()) #Fri Apr  3 22:54:29 2026

# 시간 포맷팅
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print("포맷팅된 시간:", formatted_time) #2026-04-03 22:54:29

# 년과 일로 환산
days = round(time.time() / (24 * 60 * 60), 2)
years = round(days / 365, 2)
print(f"현재까지 경과된 년수: {years}년")
print(f"현재까지 경과된 일수: {days}일")

# 시간 지연
print("3초 후에 메시지가 출력됩니다...")
time.sleep(3)
print("3초가 지났습니다!")

# 시간 측정
start_time = time.time()

# 예시: 1부터 1000000까지의 합 계산
# total = sum(range(1, 1000001))
total = 0
for i in range(1, 1000001):
    total += i

end_time = time.time()
print("총 소요 시간:", end_time - start_time, "초") 

