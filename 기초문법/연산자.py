# 연산자 - 값이나 변수에 대해 계산이나 비교 등의 작업을 수행하는 기호
# 산술, 비교, 논리 연산자
# 산술 연산자
"""
n1 = 10
n2 = 4

print("n1 + n2 =", n1 + n2)
print("n1 - n2 =", n1 - n2)
print("n1 * n2 =", n1 * n2)
print("n1 / n2 =", n1 / n2)
print("n1 // n2 =", n1 // n2) #2, 몫
print("n1 % n2 =", n1 % n2) #2, 나머지
print("n1 ** n2=", n1 ** n2) #10000, 거듭제곱
"""

# 비교 연산자
x = 10
y = -10

print(x > 0) #True
print(y > 0) #False
print()

print(x == 10) #True
print(x != 10) #False
print()

# 논리 연산자 - and, or, not
# C, Java 언어는 기호 사용 - &&, ||, ! 
result1 = (x > y) and (y == 10) # True and False
print(result1) #False

result2 = (x > y) or (y == 10) # True and False
print(result2) #True

result3 = not (x > y) #!True
print(result3) #False

# 대입 연산자(할당 연산자), '='
user_id = "cloud100"
password = "ace1234"
print("아이디 =", user_id)
print("비밀번호 =", password)

# 변수값 교환
x = 1
y = 2

print("=== 교환전 ===")
print("x =", x, ", y =", y)

# 교환(임시변수에 x값 저장, x변수에 y값 저장, y변수에 임시값 저장)
# 여러줄 주석은 """~ """
'''
temp = x
x = y
y = temp
'''

# 직접 교환
x, y = y, x

print("=== 교환후 ===")
print("x =", x, ", y =", y)


# 실습 문제
bread = 30
people = 4

share = bread // people
remain = bread % people

print("몫:", share, ", 남은 빵:", remain)

# format 출력 방식 - f""안에 변수는 중괄호로 묶는다.
print(f"몫: {share}, 남은 빵: {remain}")







































