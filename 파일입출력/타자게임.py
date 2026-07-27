
import random
import time

try:
  with open('output/word.txt', 'r', encoding='utf-8') as f:
      word = f.read().split() # 공백을 기준으로 단어 분리
      
  n = 1 #문제 번호
  print("[타자 게임] 준비되면 엔터를 누르세요")
  input() #엔터 입력 대기
  
  start = time.time() #게임 시작 시간 기록
  
  while n <= 10:
    print(f"\n문제 {n}")
    question = random.choice(word) #랜덤으로 단어 출력
    print(question)
    user = input() #사용자 입력 받기
    
    if question == user:
      print("통과!")
      n += 1 #문제 번호 증가
    else:
      print("오타! 다시 도전!")
  
  end = time.time() #게임 종료 시간 기록
  et = end - start #총 게임 시간 계산
  print(f"게임 시간: {et:.2f}초")
except FileNotFoundError:
  print("파일을 찾을 수 없습니다.")
  
  