# 함수 - 특정한 기능을 수행하는 코드 모음
# 인사하는 함수 정의(def 키워드 사용)
def greet():
    print("Hello, Python!!")
    
def greet2(name):
    print(f"Hello, {name}!!")
    
def get_gugudan(dan):
    for i in range(1, 10):
        print(f"{dan} x {i} = {dan*i}")
    
# 메인 영역 - 함수 호출(사용)
greet()
greet2("명제")
greet2("선화")
    
# 구구단 함수 호출
get_gugudan(8)

# return이 있는 함수
# 응원 메시지를 보내는 함수
def message():
    return "행운을 빌어요!"

# 제곱 계산 함수
def square(x):
    return x * x

# 두 수를 더하는 함수
def add(x, y):
    return x + y

# 메인 영역
msg = message() #문자열 반환받음
print(msg)

value1 = square(4) #16을 반환받음
print(value1)

value2 = add(4, 5) #9를 반환
print(value2)

# 도형의 면적을 계산하는 함수 정의와 사용
def square(w, h):
    return w * h

def triangle(b, h):
    return (b * h) / 2

print("사각형 면적:", square(5, 4))  # 사각형 면적: 20
print("삼각형 면적:", triangle(5, 4))  # 삼각형 면적: 10.0

