
# 날짜와 시간 다루기
from datetime import datetime, date

# 현재 날짜와 시간 - datetime
now = datetime.now()
print(now) #2026-03-29 16:07:06.140626

# 년 월 일
print(f"{now.year}년 {now.month}월 {now.day}일")

# 시 분 초
print(f"{now.hour} : {now.minute} : {now.second}")

# 오늘 날짜 - date
today = date.today()
print("오늘:", today)

# 식목일
the_day = date(2026, 8, 15)
print("광복절:", the_day)

# 날짜 차이 계산
date_diff = the_day - today
print("D-day:", date_diff.days) #D-day: 7

from datetime import datetime

# 1. 오늘 날짜와 시간 가져오기
now = datetime.now()

# 2. strftime을 이용해 원하는 형식으로 변환하기
# 참고: 요일 표시 기호(%A)는 운영체제(OS) 언어 설정에 따라 영문(Tuesday)으로 나올 수 있습니다.
formatted_date = now.strftime("%Y년 %m월 %d일 (%A)")

print(formatted_date)

