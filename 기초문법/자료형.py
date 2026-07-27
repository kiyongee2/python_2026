# 자료형 - 변수에 저장되는 데이터의 종류
# type() 함수는 데이터의 자료형을 알려주는 기능
x = 10
print(type(x)) #<class 'int'>

rate_of_birth = 0.8
print(type(rate_of_birth)) #<class 'float'>
print("대한민국의 2025년 출산율은", rate_of_birth, "입니다")

is_student = False
print(type(is_student)) #<class 'bool'>

print(4 > 5) #False
print(4 == 4) #True

say = "'힘 내세요'라고 \n말했다."  #'\n' - 줄바꿈 기호 
print(say)
print(type(say)) #<class 'str'>

# 문자열 변수 - 여러 줄 사용, '\t'
table = """
상품\t가격\t수량 
키보드\t20000\t100
마우스\t15000\t30
"""
print(table)






















