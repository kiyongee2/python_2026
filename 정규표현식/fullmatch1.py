
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
        
        