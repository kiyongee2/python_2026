
from datetime import datetime

while True:
  user_input = input("챗봇에게 질문하세요(종료하려면 '종료' 입력): ")
  if user_input == "종료":
      print("챗봇을 종료합니다.")
      break
  elif "시간" in user_input:
      now = datetime.now()
      print(f"현재 시간은 {now.hour}시 {now.minute}분입니다.")
  elif "안녕" in user_input:
      print("안녕하세요! 무엇을 도와드릴까요?")
  elif "이름" in user_input:
      print("저는 챗봇입니다. 당신의 질문에 답변해드릴 수 있어요.")
  else:
      print("죄송합니다. 이해하지 못했습니다. 다른 질문을 해주세요.")