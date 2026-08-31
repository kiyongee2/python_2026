import re

# 휴대폰 번호 검사
phone = "010-1234-5678"
if re.fullmatch(r'01[016789]-\d{3,4}-\d{4}', phone):
    print("올바른 휴대폰 번호입니다.")

# 주민등록번호 검사
jumin = "900101-1234567"
print(bool(re.fullmatch(r'\d{6}-[1-4]\d{6}', jumin)))   # True

# fullmatch() : 문자열 "전체"가 패턴과 일치하는지 검사
'''[a-zA-Z0-9._%+-]+: @ 앞부분. 영문, 숫자, ., _, %, +, -를 한 글자 이상 허용
@: 이메일의 @ 기호
[a-zA-Z0-9.-]+: 도메인 이름. 예: naver, google, my-site
\.: 실제 마침표 .
정규표현식에서 .은 아무 문자 하나를 뜻하므로, 마침표 자체는 \.로 표현합니다.
[a-zA-Z]{2,}: 최상위 도메인. 영문 2글자 이상. 예: com, kr, net'''
email = "hong@naver.com"
if re.fullmatch(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', email):
    print("올바른 이메일 형식입니다.")
else:
    print("이메일 형식이 아닙니다.")