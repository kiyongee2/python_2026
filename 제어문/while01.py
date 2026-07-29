
# 1부터 5까지 출력
n = 1
while n <= 5:
  print(n)
  n += 1

# 1부터 5까지 출력(break문)
n = 1
while True:
  if n > 5:
    break
  print(n)
  n += 1
  
# 1부터 10까지의 합
n = 1
total = 0
while n <= 5:
  total += n
  print("n=", n, ", total=", total)
  n += 1
print(total)

# 1부터 n까지의 합
'''
n = int(input("정수: "))
i = 1
total = 0
while i <= n:
  total += i
  i += 1
print(f"1부터 {n}까지의 합: {total}")
'''

# 챗봇
'''
count = 0
while True:
  msg = input("입력(종료=끝): ")
  if msg == "종료":
    print("대화를 종료합니다.")
    break
  count += 1
  # print(f"{count}:번 {msg}")
  # print(count, "번: ", msg)
'''
  
from datetime import datetime

while True:
  msg = input("챗봇에게 질문하세요(종료=끝): ")
  if msg == "종료":
      print("대화를 종료합니다.")
      break
  elif "시간" in msg:
      now = datetime.now()
      print(f"현재 시간은 {now.hour}시 {now.minute}분입니다.")
  elif "안녕" in msg:
      print("안녕하세요! 무엇을 도와드릴까요?")
  elif "이름" in msg:
      print("저는 챗봇입니다. 당신의 질문에 답변해드릴 수 있어요.")
  else:
      print("죄송합니다. 이해하지 못했습니다. 다른 질문을 해주세요.")
