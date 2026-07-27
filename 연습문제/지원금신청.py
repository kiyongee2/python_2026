
# 민생 회복 지원금
# 출생년도 끝자리 숫자에 따라 신청일이 다름
# 출생년도 4자리를 입력하세요: 1995
# 신청일은 화요일입니다.
birth_year = input("출생년도 4자리를 입력하세요: ")
last_digit = birth_year[-1] #출생년도 끝자리 숫자
year = int(birth_year)
if year < 1900 or year > 2006:
    print("출생년도는 1900년부터 2006년 사이로 입력해주세요.")
else:   
  if last_digit in ['1', '6']:
    print("신청일은 월요일입니다.")
  elif last_digit in ['2', '7']:
    print("신청일은 화요일입니다.")
  elif last_digit in ['3', '8']:
    print("신청일은 수요일입니다.")
  elif last_digit in ['4', '9']:
    print("신청일은 목요일입니다.")
  elif last_digit in ['5', '0']:
    print("신청일은 금요일입니다.")

"""
if year < 1900 or year > 2006:
    print("출생년도는 1900년부터 2006년 사이로 입력해주세요.")
else:   
  if last_digit in "16":
    print("신청일은 월요일입니다.")
  elif last_digit in "27":
    print("신청일은 화요일입니다.")
  elif last_digit in "38":
    print("신청일은 수요일입니다.")
  elif last_digit in "49":
    print("신청일은 목요일입니다.")
  elif last_digit in "50":
    print("신청일은 금요일입니다.")
"""

