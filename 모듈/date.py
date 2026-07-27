
# 날짜와 시간 다루기
from datetime import datetime, date

# 현재 날짜와 시간 출력
now = datetime.now() 
print("현재 날짜와 시간:", now)

# 특정 날짜 생성
the_day = date(2026, 5, 5)
print("어린이날:", the_day)

# 오늘 날짜 출력
today = date.today()
print("오늘 날짜:", today)

# 날짜 차이 계산
date_diff = the_day - today
print("어린이날까지 남은 일수:", date_diff.days)

# 날짜 포맷팅
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print("포맷팅된 날짜와 시간:", formatted_date)