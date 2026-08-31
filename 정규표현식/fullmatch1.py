
import re 

'''def validate_phone_number(phone):
    pattern = r"\d{3}-\d{3,4}-\d{4}"
    if re.fullmatch(pattern, phone):
        return True
    return False'''
  
def validate_phone_number(phone):
    pattern = r"\d{3}-\d{3,4}-\d{4}"
    return bool(re.fullmatch(pattern, phone))
  
phone_list = [
    "010-1234-5678",
    "010-123-5678",
    "010-12345-5678",
    "010-1234-56789",
    "01012345678",
]

for phone in phone_list:
    if validate_phone_number(phone):
        print(f"{phone}는 유효한 전화번호입니다.")
    else:
        print(f"{phone}는 유효하지 않은 전화번호입니다.")
        
# 비밀번호 유효성 검사
pw = input("비밀번호를 입력하세요: ")
# 영문 또는 숫자 조합, 8자 이상인지 검사
if re.fullmatch(r'[a-zA-Z0-9]{8,}', pw):
    print("사용 가능한 비밀번호입니다.")
else:
    print("영문과 숫자로 8자 이상 입력하세요.")
        

# 영문이 최소 1개, 숫자가 최소 1개,
# 그리고 영문과 숫자로만 구성되며 8자 이상인지 검사
if re.fullmatch(r'(?=.*[a-zA-Z])(?=.*[0-9])[a-zA-Z0-9]{8,}', pw):
    print("사용 가능한 비밀번호입니다.")
else:
    print("영문과 숫자를 포함하여 8자 이상 입력하세요.")
        