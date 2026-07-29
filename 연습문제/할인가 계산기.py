# 할인가 계산하기
'''
price = int(input("가격 입력: "))
discount = float(input("할인율(%) 입력: "))

discount_rate = discount / 100  # 소수로 환산 
cost = price + int(price * discount_rate) # 금액 = 가격 x 할인율

print("최종 결제 금액:", cost)
'''

# 윤년 계산하기
'''
year = int(input("연도: "))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f"{year}년은 윤년입니다.")
else:
    print(f"{year}년은 평년입니다")
'''

# 접종 요일 안내(접종대상 0 ~ 100)
# 출생연도를 입력받아 끝자리 숫자로 접종 요일 안내
'''
year = int(input("출생 연도: "))
last_num = year % 10

if year < 1926 or year > 2006:
    print("출생연도는 1926년부터 2006년 사이로 입력해주세요")
else:
    if last_num == 1 or last_num == 6:
        print("월요일")
    elif last_num == 2 or last_num == 7:
        print("화요일")
    elif last_num == 3 or last_num == 8:
        print("수요일")
    elif last_num == 4 or last_num == 9:
        print("목요일")
    else:
        print("금요일")
'''
# 출생연도를 입력받아 끝자리 문자로 접종 요일 안내
birth_year = input("출생 연도: ")
last_digit = birth_year[-1]
year = int(birth_year)

if year < 1926 or year > 2006:
    print("출생연도는 1926년부터 2006년 사이로 입력해주세요")
else:
    """
    if last_digit == '1' or last_digit == '6':
        print("월요일")
    elif last_digit == '2' or last_digit == '7':
        print("화요일")
    elif last_digit == '3' or last_digit == '8':
        print("수요일")
    elif last_digit == '4' or last_digit == '9':
        print("목요일")
    else:
        print("금요일")
    """
    if last_digit in ['1', '6']:
        print("월요일")
    elif last_digit in ['2', '7']:
        print("화요일")
    elif last_digit in ['3', '8']:
        print("수요일")
    elif last_digit in ['4', '9']:
        print("목요일")
    else:
        print("금요일")





















    
