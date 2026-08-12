
import calendar

# 2026년 전체 달력 출력
calendar.prcal(2026)

# 2026년 8월 달력 출력
calendar.prmonth(2026, 8)

# 요일 이름 출력
print("요일 이름:", calendar.day_name[0])  # 월요일
print("요일 이름:", calendar.day_name[6])  # 일요일

print("요일 리스트:", calendar.day_name[:]) 

# 특정 날짜의 요일 변환
day_of_week = calendar.weekday(2026, 8, 15) 
print(day_of_week)  # 5
print(calendar.day_name[day_of_week])  # 토요일

# 윤년 여부 확인
is_leap = calendar.isleap(2024)
print(is_leap)  # True