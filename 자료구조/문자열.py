# 문자를 저장한 리스트
my_list = ['h', 'e', 'l', 'l', 'o']
print(my_list)
print(my_list[0]) # h
print(my_list[-1]) # 0
print(my_list[0:-1]) # ['h', 'e', 'l', 'l']
print(len(my_list)) #5

# 문자열 - 특별한 1차원 리스트
greeting = "hello"
print(greeting[0]) # h
print(greeting[-1]) # 0
print(greeting[0:-1]) # hell
print(len(greeting)) #5

# 대소문자 변환
print("소문자 변환:", greeting.lower()) #hello
print("대문자 변환:", greeting.upper()) #HELLO 

# 문자열 변경 - replace(변경전 문자, 변경후 문자)
s = "Hello, World"
print(s.replace('World', 'Korea')) #Hello, Korea

# 특정 문자의 시작 위치(인덱스) 찾기 - find(문자)
print(s)
print("문자열에서 'World'의 위치:", s.find('World')) #7
# 찾는 문자가 문자열에 없으면 -1을 반환
print("문자열에서 'World'의 위치:", s.find('Seoul')) #-1

# split() -> 문자열을 구분기호로 분리하는 함수
csv = "apple,banana,strawberry"
fruits = csv.split(',') #문자열이 리스트형태로 변환됨
print(fruits) #['apple', 'banana', 'strawberry']
print(fruits[0]) #apple
print(fruits[-1]) #strawberry

# strip() -> 문자열의 양쪽 공백 제거
s2 = "   Hello, World!   "
print(s2.strip()) #Hello, World!
print(s2.lstrip()) #Hello, World!, 왼쪽 공백 제거
print(s2.rstrip()) #   Hello, World!, 오른쪽 공백 제거

s = "Python"
print(s[0])       # P
print(s[0:3])     # Pyt
print(s[-1])      # n
print(s[::2])     # Pto

fruit = "banana,grape,kiwi"
fruit_list = fruit.split(",") # 리스트로 분리
print(fruit_list)     
print(fruit_list[0])
print(fruit_list[1])

print("Hello".replace("l", "L")) # 문자 수정
print("  hi  ".strip()) # 공백 제거

info = "홍길동 / 010-1234-5678 / 서울"
info_list = info.split(' / ')
print(info_list)