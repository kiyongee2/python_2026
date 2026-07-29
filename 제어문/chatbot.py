# 미니 챗봇 프로그램
"""
while True:
  msg = input("입력(종료=끝): ")
  if msg == "종료":
    print("대화를 종료합니다.")
    break
  print("입력한 말:", msg)
"""

count = 0
while True:
  msg = input("입력(종료=끝): ")
  count += 1
  if msg == "종료":
    print("대화를 종료합니다.")
    break
  
  print(count, "번:", msg)
